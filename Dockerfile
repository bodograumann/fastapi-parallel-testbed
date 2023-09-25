FROM ghcr.io/br3ndonland/inboard:fastapi-0.56-python3.11-slim as service

COPY ./main.py /app/main.py

ENV LOG_LEVEL=DEBUG
ENV MAX_WORKERS=1
ENV APP_MODULE=main:app

EXPOSE 80
