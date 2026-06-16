🛡️ Phishing Website Detection

An end-to-end Machine Learning system for detecting phishing websites using URL and website security features. The project follows a production-style ML workflow including data ingestion, validation, transformation, model training, experiment tracking, and API-based prediction.

🚀 Features
 
- Automated Data Ingestion from MongoDB
- Data Validation & Drift Detection
- Feature Engineering & Preprocessing
- Hyperparameter Tuning
- Multiple Model Evaluation
- MLflow Experiment Tracking
- DagsHub Integration
- FastAPI Prediction API
- Batch Prediction using CSV Files

📊 Workflow

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

🧠 Models Evaluated

- Random Forest Classifier
- Gradient Boosting Classifier 
- AdaBoost Classifier

🛠️ Tech Stack

Language: Python

ML Libraries: Scikit-Learn, Pandas, NumPy

Database: MongoDB

Experiment Tracking: MLflow, DagsHub

API Framework: FastAPI

📌 Problem Statement

Phishing websites imitate legitimate websites to steal sensitive information such as passwords, banking credentials, and personal data. This project uses machine learning techniques to automatically classify websites as phishing or legitimate based on security-related website features.

🎯 Output

The system accepts website feature data in CSV format and predicts:

- 1 → Phishing Website
- 0 → Legitimate Website

Predictions are returned through the FastAPI endpoint and appended as a new prediction column.

🌐 API Endpoints

Endpoint| Method| Description
"/"| GET| API Home
"/train"| GET| Train the ML Pipeline
"/predict"| POST| Generate Predictions from CSV Input
"/docs"| GET| Swagger API Documentation

⚙️ Run Locally

git clone <https://github.com/sahilkhn-03/networksecurity.git>

cd <networksecurity>

pip install -r requirements.txt

python app.py

Open:

http://localhost:8000/docs
