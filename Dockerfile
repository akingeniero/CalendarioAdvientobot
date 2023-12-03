FROM python:3.9

WORKDIR /app

RUN pip install pyTelegramBotAPI Flask pytz

COPY app/ .

EXPOSE 8080

CMD ["python", "CalendarioAdvientoBot.py"]