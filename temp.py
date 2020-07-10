from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('default_credit_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index-temp.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        LIMIT_BAL = int(request.form['LIMIT_BAL'])
        AGE=int(request.form['AGE'])
        BILL_AMT1 =int(request.form['BILL_AMT1'])
        BILL_AMT2 =int(request.form['BILL_AMT2'])
        BILL_AMT3 =int(request.form['BILL_AMT3'])
        BILL_AMT4 =int(request.form['BILL_AMT4'])
        BILL_AMT6 =int(request.form['BILL_AMT6'])
        PAY_AMT1 =int(request.form['PAY_AMT6'])
        PAY_AMT6 =int(request.form['PAY_AMT6'])
        
        PAY_0=int(request.form['PAY_0'])
        PAY_2=int(request.form['PAY_2'])
        
        prediction=model.predict([[LIMIT_BAL,AGE,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT6,PAY_AMT1,PAY_AMT6,PAY_0,PAY_2]])
        
        if prediction == 1:
            prediction = "The Client will have default payment"
        else:
            prediction =  "The Client will have no default payment"
        print("Prediction", prediction)
        return render_template('index-temp.html',prediction_text="The model predicts that-  {}".format(prediction))
    else:
        return render_template('index-temp.html')

if __name__=="__main__":
    app.run(debug=True)

