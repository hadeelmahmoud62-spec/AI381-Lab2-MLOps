# Stage 1: Install dependencies
FROM python:3.13.5-slim AS builder

WORKDIR /install

COPY requirementslab2.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirementslab2.txt


# Stage 2: Run the application
FROM python:3.13.5-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /install /usr/local
COPY src/ ./src/
COPY model.joblib .

# Create a non-root user
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 10001 appuser

USER appuser

EXPOSE 8000

# Check whether the API is healthy
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)" || exit 1

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]