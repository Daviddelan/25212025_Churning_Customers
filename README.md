# 25212025_Churning_Customers
This project seeks to presict whether customers would churn following when given information about the users. This projects predicts customer churning using a Multi-Layer Perceptron trained using Functional API.
The project would help users to predict customers churning and the model was trained using a dataset from a telecommunications company, consisting of customer profiles and their churn status. 
The goal is to develop a model that can accurately identify customers at high risk of churning. And the model has an accuracy of about 85%.

As stated, this project trained an MLP implement with Keras using the Functional API.
To train the dataset, the dataset was preprocessed and the important features were estracted so tha the features with the highest correlation were used. 
In order to calculate the performance of the MLP it was evaluated using accuracy and AUC scores.

The optimized model of the MLP used 15 features in total. 
These features were : 
TotalCharges
MonthlyCharges
tenure
Contract
PaymentMethod
OnlineSecurity
TechSupport
gender
InternetService
OnlineBackup
PaperlessBilling
Partner
MultipleLines
DeviceProtection
SeniorCitizen

The demonstration of how to use the model which was deployed can be found in this youtube video: https://youtu.be/xGfO-lTcsXM
