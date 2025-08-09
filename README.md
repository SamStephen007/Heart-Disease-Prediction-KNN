# Heart Disease Prediction App (KNN Model)

This is a simple Flask web application that predicts whether a person has heart disease based on six features using a trained KNN model.

## 📂 Project Structure

```
.
├── app.py                # Main Flask application
├── knn_model.pkl         # Saved trained KNN model
├── scaler.pkl            # Saved StandardScaler
├── templates/
│   └── index.html        # HTML form for input
└── README.md             # Project documentation
```

## 🚀 How to Run

1. **Clone the repository or download files**

2. **Install dependencies**:
```bash
pip install flask
```

3. **Ensure the following files are in the same directory**:
   - `app.py`
   - `knn_model.pkl`
   - `scaler.pkl`
   - `templates/index.html`

4. **Run the Flask app**:
```bash
python app.py
```

5. **Open the application in your browser**:
```
http://127.0.0.1:5000
```

## 📌 Input Features

The model expects **6 numerical inputs**:
1. `age` - Age of the patient
2. `trestbps` - Resting blood pressure (mm Hg)
3. `chol` - Serum cholesterol (mg/dl)
4. `thalach` - Maximum heart rate achieved
5. `oldpeak` - ST depression induced by exercise
6. `ca` - Number of major vessels (0-3) colored by fluoroscopy

## 🧠 Model

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Preprocessing**: StandardScaler
- **Dataset**: Heart Disease dataset from Kaggle

## 🖼 Example

Form inputs:

| Age | trestbps | chol | thalach | oldpeak | ca |
|-----|----------|------|---------|---------|----|
| 63  | 145      | 233  | 150     | 2.3     | 0  |

Prediction: `Heart Disease`

---
## Screen Shots and Visualization
![HeartDisease](Images\Figure_1.png)
![HeartDisease](Images\safe.png)
![HeartDisease](Images\danger.png)

## Author

Sam Stephen

## contact

stephensam0770@gmail.com