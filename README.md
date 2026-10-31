# AI381 Lab 2 – MLOps Churn Prediction API

A machine learning project that demonstrates an end-to-end MLOps workflow using Python, FastAPI, Docker, GitHub Actions, Trivy, and GitHub Container Registry.

## Project Overview

This project predicts customer churn using a trained machine learning model.

The project includes:
- Model training and serialization using Joblib.
- REST API built with FastAPI.
- Input validation using Pydantic.
- Automated testing using Pytest.
- Docker containerization.
- Continuous Integration using GitHub Actions.
- Security vulnerability scanning using Trivy.
- Automated Docker image publishing to GHCR.

## Project Structure

```text
.
├── src/
│   ├── app/
│   │   └── main.py
│   └── train/
│       └── train.py
├── tests/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── docker-publish.yml
├── Dockerfile
├── requirementslab2.txt
├── model.joblib
└── README.md

Run Locally
Install dependencies:
pip install -r requirementslab2.txt

Run the API:
python -m uvicorn src.app.main:app --host 0.0.0.0 --port 8000

API documentation:
http://localhost:8000/docs⁠
Health check:
http://localhost:8000/health⁠


Run Tests:
python -m pytest -v

Docker
Build the Docker image:
docker build -t ai381-churn-api .
Run the container:
docker run -p 8000:8000 ai381-churn-api



CI/CD Pipeline
GitHub Actions automates the following processes:
1 Linting and automated testing.
2 Docker image building.
3 Security scanning using Trivy.
4 Publishing the Docker image to GHCR.

Docker Image – GHCR
Image:
ghcr.io/hadeelmahmoud62-spec/ai381-lab2-mlops
Image Digest:
sha256:c91bcae8110b3de758a047d3fe8d88568cef896d05135d2581e9edf4116b5a7d

Technologies Used:
Python
Scikit-learn
FastAPI
Pydantic
Pytest
Docker
GitHub Actions
Trivy
GitHub Container Registry