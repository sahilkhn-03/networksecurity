# 🛡️ Phishing Website Detection

An end-to-end machine learning project to detect phishing websites using URL and security-related website features.  
It follows a production-style pipeline covering ingestion, validation, transformation, model training, experiment tracking, and API prediction.

## 🚀 Features

- Automated data ingestion from MongoDB
- Data validation and drift detection
- Feature engineering and preprocessing
- Hyperparameter tuning
- Multi-model training and evaluation
- MLflow experiment tracking
- DagsHub integration
- FastAPI-based prediction API
- Batch prediction from CSV files

## 📊 Workflow

```text
MongoDB
  ↓
Data Ingestion
  ↓
Data Validation
  ↓
Data Transformation
  ↓
Model Training
  ↓
Model Evaluation
  ↓
Model Serialization
  ↓
FastAPI Prediction Service
```

## 🧠 Models Evaluated

- Random Forest Classifier
- Gradient Boosting Classifier
- AdaBoost Classifier

## 🛠️ Tech Stack

- **Language:** Python
- **ML Libraries:** Scikit-learn, Pandas, NumPy
- **Database:** MongoDB
- **Experiment Tracking:** MLflow, DagsHub
- **API Framework:** FastAPI

## 📌 Problem Statement

Phishing websites mimic legitimate websites to steal sensitive information such as passwords, banking credentials, and personal data.  
This project applies machine learning to classify websites as **phishing** or **legitimate** using security-focused features.

## 🎯 Output

The system accepts website feature data in CSV format and predicts:

- `1` → Phishing website
- `0` → Legitimate website

Predictions are returned through the FastAPI endpoint and appended as a new `prediction` column.

## 🌐 API Endpoints

| Endpoint   | Method | Description                                |
|------------|--------|--------------------------------------------|
| `/`        | GET    | API home                                   |
| `/train`   | GET    | Train the machine learning pipeline        |
| `/predict` | POST   | Generate predictions from CSV input        |
| `/docs`    | GET    | Swagger API documentation                  |

## ⚙️ Run Locally

```bash
git clone https://github.com/sahilkhn-03/networksecurity.git
cd networksecurity
pip install -r requirements.txt
python app.py
```

Open: `http://localhost:8000/docs`
