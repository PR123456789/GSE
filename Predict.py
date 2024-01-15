from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>To predict future demand send a POST request to /predict!</h1>"

@app.route("/predict", methods=["POST"])
def predict():
    if lr:
        json_ = request.json
        print(json_)
        df = pd.DataFrame(json_)
        df["DateTime"] = df["DateTime"].apply(lambda x: pd.to_datetime(x))
        df["Weekday"] = df["DateTime"].apply(lambda x: x.weekday())
        df["Weekday"] = df["Weekday"].map({0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"})
        df = pd.get_dummies(df, columns=["Weekday"], prefix="", prefix_sep="", dtype=float)
        df = df.reindex(columns=model_columns, fill_value=0)
        timeseries = df.values
        timeseries = timeseries[np.newaxis, :, :]

        prediction = lr.predict(timeseries)

        return jsonify({"prediction": str(prediction[0,0])})
    else:
        print ("Train the model first")
        return ("No model here to use")


if __name__ == "__main__":
    with open("./Model/bestmodel.pkl", "rb") as f:
        lr = pickle.load(f)
    print ("Model loaded")
    with open("./Model/model_columns.pkl", "rb") as f:
        model_columns = pickle.load(f)
    print ("Columns loaded")

    app.run(port=5000, debug=True)