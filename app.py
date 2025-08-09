from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model and scaler
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        features = [
            float(request.form['age']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['thalach']),
            float(request.form['oldpeak']),
            float(request.form['ca'])
        ]
        
        # Prepare the input
        sample = np.array([features])
        sample_scaled = scaler.transform(sample)

        # Predict
        prediction = model.predict(sample_scaled)[0]
        result = "Heart Disease Detected" if prediction == 0 else "No Heart Disease Detected"
        result_class = "danger" if prediction == 0 else "success"

        return render_template('index.html', 
                             prediction_text=result,
                             result_class=result_class,
                             show_result=True)

    except Exception as e:
        return render_template('index.html', 
                             prediction_text=f"Error: {str(e)}",
                             result_class="warning",
                             show_result=True)

if __name__ == '__main__':
    app.run(debug=True)