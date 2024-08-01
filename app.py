from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('model/churn_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [int(request.form['SeniorCitizen']),
                int(request.form['tenure']),
                float(request.form['MonthlyCharges']),
                int(request.form['Partner_encoded']),
                int(request.form['Dependents_encoded']),
                int(request.form['OnlineSecurity_encoded']),
                int(request.form['OnlineBackup_encoded']),
                int(request.form['DeviceProtection_encoded']),
                int(request.form['TechSupport_encoded']),
                int(request.form['Contract_encoded']),
                int(request.form['PaperlessBilling_encoded']),
                int(request.form['PaymentMethod_encoded'])]
    
    # Scale the features
    features = scaler.transform([features])
    
    # Predict churn
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        prediction_text = "The customer is likely to churn."
    else:
        prediction_text = "The customer is not likely to churn."
    
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
