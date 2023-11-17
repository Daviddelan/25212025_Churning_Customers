from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your model and other necessary objects like scaler and encoder
model = pickle.load(open('/Users/daviddela/Flask/Assignment/churning_model.pkl', 'rb'))
scaler = pickle.load(open('/Users/daviddela/Flask/Assignment/standard_scaler.pkl', 'rb'))
one_hot_encoder = pickle.load(open('/Users/daviddela/Flask/Assignment/onehot_encoder.pkl', 'rb'))

@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            # Extract numerical features directly
            total_charges = float(request.form.get('totalCharges', 0))
            monthly_charges = float(request.form.get('monthlyCharges', 0))
            tenure = float(request.form.get('tenure', 0))
            
            # Extract categorical features
            
            contract= request.form.get('contract')
            payment_method = request.form.get('paymentMethod')
            online_security = request.form.get('onlineSecurity')
            tech_support = request.form.get('techSupport')
            gender = request.form.get('gender')
            internet_service = request.form.get('internetService')
            online_backup = request.form.get('onlineBackup')
            paperless_billing = request.form.get('paperlessBilling')
            partner = request.form.get('partner')
            multiple_lines = request.form.get('multipleLines')
            device_protection = request.form.get('deviceProtection')
            senior_citizen = request.form.get('seniorCitizen')
        
            final_features = [total_charges, monthly_charges, tenure, contract,payment_method,online_security,tech_support, gender, internet_service, online_backup, paperless_billing, partner,multiple_lines,device_protection,senior_citizen]
            final_features_encoded = one_hot_encoder.fit_transform([final_features])
            final_features_dense = final_features_encoded.toarray()
            final_features_scaled = scaler.transform(final_features_dense)
            prediction = model.predict(final_features_scaled)
            confidence_interval = '85%'

            # Return the prediction result
            return render_template('submit.html', prediction=prediction, confidence_interval=confidence_interval)
        
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('submit.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
