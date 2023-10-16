import pickle
import os
from flask import Flask
from flask import request
from flask import jsonify


model_file = "model2.bin"
dv_file = "dv.bin"

app = Flask('creditscore')

def load_model():
    with open(model_file,'rb') as f_in:
      model = pickle.load(f_in)

    with open(dv_file,'rb') as dv_in:
     dv = pickle.load(dv_in)  


     return model,dv
    
def predict_credit_score(client):
    model,dv = load_model()
    
    X= dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]
    print(y_pred)
    return y_pred
    # credit = y_pred[1] > 0.5

@app.route('/creditscore',methods=['POST'])
def predict():
    client = request.get_json()
    y_pred = predict_credit_score(client)
    print(y_pred)
    print(type(y_pred))
    # credit = y_pred > 0.5

    result = {
       'client_get_credit_probablity': float(y_pred)
    #    'credit_approved':bool(credit)

    }
    return jsonify(result)

@app.route('/test',methods=['GET'])
def tets():
    return "Hello"

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0',port=9696)