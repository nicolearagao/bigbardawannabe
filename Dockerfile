FROM python:3.11

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-root

COPY tracker /app/tracker

CMD ["poetry", "run", "uvicorn", "tracker.api.server:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]
