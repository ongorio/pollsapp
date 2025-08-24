FROM python:3.11-slim AS builder

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS runner

RUN useradd -m -r ongorio && \
    mkdir /app && \
    chown -R ongorio:ongorio /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/


WORKDIR /app

COPY --chown=ongorio:ongorio . .

WORKDIR /app/src

USER ongorio

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "pollapp.wsgi:application"]
