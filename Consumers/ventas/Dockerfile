FROM python:3.12.0a1-alpine3.16

WORKDIR /usr/local/bin

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "consumer-ventas.py"]