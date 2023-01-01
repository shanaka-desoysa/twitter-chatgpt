FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY twitter_bot.py .

CMD ["python", "twitter_bot.py"]
