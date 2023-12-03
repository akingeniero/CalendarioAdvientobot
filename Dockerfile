FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install pyTelegramBotAPI

COPY app/ .

CMD ["python", "bot_telegram.py"]