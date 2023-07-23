from flask import Flask, render_template, request

app = Flask(__name__)

# Replace this with your actual machine learning model
def predict_fish(weight, length1, length2, length3, height, width):
    # Mocking the prediction by returning a fixed class label
    return "Trout"

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
