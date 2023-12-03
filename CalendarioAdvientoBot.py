import telebot
from flask import Flask, request

TOKEN = 'tu_token_de_telegram'

bot = telebot.TeleBot(TOKEN)
opened_gifts = {}

app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://tu_url_de_tu_servidor/' + TOKEN)
    return "!", 200

@app.route('/start', methods=['GET', 'POST'])
def hola():
    mensaje_bienvenida = (
        # Tu mensaje de bienvenida actual
    )
    return mensaje_bienvenida

@app.route('/regalo', methods=['GET', 'POST'])
def regalo():
    today = datetime.date.today()
    user = request.from_user.id
    # Resto de tu lógica para los regalos...

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    bot.polling(none_stop=True)
