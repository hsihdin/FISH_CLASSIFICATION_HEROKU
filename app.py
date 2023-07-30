from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import Normalizer
import pandas as pd
import numpy as np


app = Flask(__name__)

def predict_fish(data):
    # Load the Pickle model during app startup
    with open('FISH_CLASSIFICATION_MODEL_SVC.pkl', 'rb') as file:
        model = pickle.load(file)

    # Create a 2D array with a single row containing the feature values
    features = data

    # Make predictions using the loaded model
    prediction = model.predict(features)

    # Given dictionary mapping fish species names to numeric labels
    fish_species_dict = {
        0: "Bream",
        1: "Roach",
        2: "Whitefish",
        3: "Parkki",
        4: "Perch",
        5: "Pike",
        6: "Smelt"
    }

    # Assuming 'prediction' contains the numeric label predicted by the model
    predicted_label = prediction[0]
    predicted_species = fish_species_dict.get(predicted_label)

    return predicted_species

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    weight = float(request.form["weight"])
    length1 = float(request.form["length1"])
    length2 = float(request.form["length2"])
    length3 = float(request.form["length3"])
    height = float(request.form["height"])
    width = float(request.form["width"])

    data_dict = {
    "Weight": [weight],
    "Length1": [length1],
    "Length2": [length2],
    "Length3": [length3],
    "Height": [height],
    "Width": [width]
    }

    data = pd.DataFrame(data_dict)

    norms= Normalizer().fit(data)
    data_norms=norms.transform(data)
    data_norms= np.asarray(data_norms)

    nomred_data = pd.DataFrame(data_norms)


    predicted_fish = predict_fish(nomred_data)

    return render_template("result.html", predicted_fish=predicted_fish)

if __name__ == "__main__":
    app.run(debug=True)
