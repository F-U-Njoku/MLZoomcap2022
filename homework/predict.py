
import pickle
import warnings
from flask import Flask
from flask import request
from flask import jsonify

warnings.filterwarnings('ignore')

model = "model2.bin"
vectorizer = "dv.bin"


with open(model, "rb") as f_in:
    lr = pickle.load(f_in)
    
with open(vectorizer, "rb") as f_in:
    dv = pickle.load(f_in)
    
app = Flask("credit")

@app.route("/predict", methods=["POST"])

def predict():
    client = request.get_json()
    
    x = dv.transform([client])
    y_pred = round(lr.predict_proba(x)[0, 1], 4)
    add_card = y_pred >= 0.5
    
    response = {
        "Get card probability": y_pred,
        "Decision": bool(add_card)
    }
    
    return jsonify(response)


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
