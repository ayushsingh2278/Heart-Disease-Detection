from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and columns from pickle files
with open('randomforest_heart.pkl', 'rb') as f:
    model = pickle.load(f)

with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

# Define a function to make predictions
def predict(features):
    # Convert features to a numpy array
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
    
    # Make prediction using the loaded model
    prediction = model.predict([feature_array])[0]
    
    # Return the prediction result
    if prediction == 0:
        return "Congratulations! You are not prone to heart disease."
    else:
        return "Unfortunately, you are prone to heart disease. Please consult a doctor for further evaluation.\n or wait for our recommendation system"

# Define the routes for the Flask application
@app.route('/', methods=['GET', 'POST'])
def heart_disease_prediction():
    if request.method == 'POST':
        # Collecting features from the form
        features = {
            'Age': float(request.form.get('Age')),
            'Sex': float(request.form.get('Sex')),
            'Chestpaintype': float(request.form.get('Chestpaintype')),
            'BP': float(request.form.get('BP')),
            'Cholestrol': float(request.form.get('Cholestrol')),
            'FBS_over_120': float(request.form.get('FBS_over_120')),
            'ekg': float(request.form.get('ekg')),
            'MaxHR': float(request.form.get('MaxHR')),
            'chest_pain_exercise': float(request.form.get('chest_pain_exercise')),
            'ST': float(request.form.get('ST')),
            'Slope': float(request.form.get('Slope')),
            'vessels': float(request.form.get('vessels')),
            'Thallium': float(request.form.get('Thallium'))
        }
        
        # Use the predict function to make a prediction
        prediction_statement = predict(features)
        return render_template('result.html', prediction=prediction_statement)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
