from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and columns
with open('randomforest_heart.pkl', 'rb') as f:
    model = pickle.load(f)

with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def heart_disease_prediction():
    if request.method == 'POST':
        features = {
            'Age': float(request.form['Age']),
            'Sex': int(request.form['Sex']),
            'Chestpaintype': int(request.form['Chestpaintype']),
            'BP': float(request.form['BP']),
            'Cholestrol': float(request.form['Cholestrol']),
            'FBS_over_120': int(request.form['FBS_over_120']),
            'ekg': int(request.form['ekg']),
            'MaxHR': float(request.form['MaxHR']),
            'chest_pain_exercise': int(request.form['chest_pain_exercise']),
            'ST': float(request.form['ST']),
            'Slope': int(request.form['Slope']),
            'vessels': int(request.form['vessels']),
            'Thallium': int(request.form['Thallium'])
        }

        prediction = predict(features)

        return render_template('result.html', prediction=prediction)
    
    return '''
        <form method="post">
            <!-- Your input fields here -->
            <input type="submit" value="Submit">
        </form>
    '''

def predict(features):
    feature_array = np.array([
        features['Age'],
        features['Sex'],
        features['Chestpaintype'],
        features['BP'],
        features['Cholestrol'],
        features['FBS_over_120'],
        features['ekg'],
        features['MaxHR'],
        features['chest_pain_exercise'],
        features['ST'],
        features['Slope'],
        features['vessels'],
        features['Thallium']
    ], dtype=np.float32)
    
    prediction = model.predict([feature_array])[0]
    
    return "Congratulations! You are not prone to heart disease." if prediction == 0 else "Unfortunately, you are prone to heart disease. Please consult a doctor for further evaluation."

if __name__ == '__main__':
    app.run(debug=True)
