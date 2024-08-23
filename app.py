@app.route('/', methods=['GET', 'POST'])
def heart_disease_prediction():
    if request.method == 'POST':
        try:
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
        except KeyError as e:
            return f"Missing data for {str(e)}", 400
        except ValueError as e:
            return f"Invalid value provided: {str(e)}", 400

    return '''
        <form method="post">
            Age: <input type="text" name="Age"><br>
            Sex (1 for male, 0 for female): <input type="text" name="Sex"><br>
            Chestpaintype: <input type="text" name="Chestpaintype"><br>
            BP: <input type="text" name="BP"><br>
            Cholestrol: <input type="text" name="Cholestrol"><br>
            FBS_over_120 (1 for yes, 0 for no): <input type="text" name="FBS_over_120"><br>
            EKG: <input type="text" name="ekg"><br>
            MaxHR: <input type="text" name="MaxHR"><br>
            Chest pain exercise (1 for yes, 0 for no): <input type="text" name="chest_pain_exercise"><br>
            ST: <input type="text" name="ST"><br>
            Slope: <input type="text" name="Slope"><br>
            Vessels: <input type="text" name="vessels"><br>
            Thallium: <input type="text" name="Thallium"><br>
            <input type="submit" value="Submit">
        </form>
    '''
