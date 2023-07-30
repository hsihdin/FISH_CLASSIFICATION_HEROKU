from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

# Replace this with your actual machine learning model
def predict_fish(weight, length1, length2, length3, height, width):
    # Load the Pickle model during app startup
    with open('FISH_CLASSIFICATION_MODEL_SVC.pkl', 'rb') as file:
        model = pickle.load(file)
    prediction = model.predict([[weight, length1, length2, length3, height, width]])

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

    # Mocking the prediction by returning a fixed class label
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

    predicted_fish = predict_fish(weight, length1, length2, length3, height, width)

    return render_template("result.html", predicted_fish=predicted_fish)

if __name__ == "__main__":
    app.run(debug=True)
