yimport numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from tensorflow.keras.models import load_model

import numpy as np

app = Flask(__name__)
loaded_model = load_model("heart.h5")
model = load_model("CESAREAN.h5")

@app.route('/')
def main():
    return render_template("main.html")


@app.route('/heart')
def heart():
    return render_template("index.html")

@app.route('/ces')
def ces():
    return render_template("ces.html")



@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list))
        result = loaded_model.predict([[to_predict_list]]) 
    if int(result)== 0:
        prediction ='NORMAL' 
    elif int(result)== 1:
        prediction ='CESAREAN'            
    return render_template("result.html", prediction = prediction) 

@app.route('/predict2',methods=['POST','GET'])
def predict2():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list))
        result = model.predict([[to_predict_list]]) 
        
    if int(result)== 0:
        prediction ='NORMAL' 
    elif int(result)== 1:
        prediction ='CESAREAN'            
    return render_template("result2.html", prediction = prediction)
                  
if __name__ == "__main__":
    app.run(debug=True)
