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
1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd fraud-detection-project