from fastapi.testclient import TestClient

from src.app.main import app, model

client = TestClient(app)

SAMPLE_CUSTOMER = {
    "tenure_months": 5,
    "monthly_fee": 89.9,
    "contract": "month-to-month",
    "internet_service": "fiber",
    "support_calls": 3,
}


def test_api_contract():
    health_response = client.get("/health")

    assert health_response.status_code == 200
    assert health_response.json() == {"status": "ok"}

    prediction_response = client.post(
        "/predict",
        json=SAMPLE_CUSTOMER,
    )

    assert prediction_response.status_code == 200
    assert set(prediction_response.json()) == {"churn_probability"}


def test_model_is_loaded():
    assert model is not None


def test_input_schema():
    response = client.post("/predict", json=SAMPLE_CUSTOMER)

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result["churn_probability"], float)
    assert 0.0 <= result["churn_probability"] <= 1.0


def test_negative_tenure_is_rejected():
    customer = SAMPLE_CUSTOMER.copy()
    customer["tenure_months"] = -1

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_prediction_is_deterministic():
    first_response = client.post("/predict", json=SAMPLE_CUSTOMER)
    second_response = client.post("/predict", json=SAMPLE_CUSTOMER)

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json() == second_response.json()