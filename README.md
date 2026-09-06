# Fraud Detection System

A production-ready, scalable framework for detecting fraudulent transactions, designed with MLOps best practices in mind.

## 🚀 Overview
This project provides an automated pipeline for fraud detection, incorporating data processing, model training, and a real-time inference interface. It focuses on modularity, experiment tracking, and containerization readiness.

## 🛠 Tech Stack (Senior MLOps Standards)
The following tools were utilized to ensure professional development and lifecycle management:

- **Language**: Python 3.12
- **Machine Learning**: `scikit-learn` (Random Forest Classifier for robust baseline modeling)
- **Experiment Tracking**: `MLflow` (For model versioning, parameter logging, and experiment traceability)
- **Deployment & UI**: `Streamlit` (For rapid, interactive dashboarding and inference visualization)
- **Environment Management**: `venv` (Ensuring dependency isolation and environment consistency)
- **Versioning**: `Git` (For source control and collaborative development)
- **Serialization**: `joblib` (Efficient model persistence for production deployment)

## 🏗 Project Architecture
- `src/train.py`: Training script with integrated MLflow logging.
- `app.py`: Streamlit-based UI for real-time fraud prediction.
- `model.pkl`: Serialized model artifact.
- `.gitignore`: Standardized exclusions to maintain repository hygiene (ignoring `venv/`, `mlruns/`, and cache).

## ⚙️ How to Setup
## 🌐 Live Demo
The application is designed to run locally using Streamlit. After following the setup instructions, the UI will be available at:
`http://localhost:8501`

## Senior engineering notes

Fraud labels are imbalanced, so accuracy is not a sufficient metric. Track precision, recall, PR-AUC, calibration, threshold economics, leakage checks, and time-aware validation. Add monitoring and a human-review path before automated decisions.
