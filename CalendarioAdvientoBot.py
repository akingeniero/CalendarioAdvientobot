import telebot
import datetime


TOKEN = '6976560783:AAFFdWfbYsegezOqNKmt0rXzCvSaEvfS-Aw'


bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)



opened_gifts = {}


@bot.message_handler(commands=['start'])
def hola(message):
    mensaje_bienvenida = (
        "¡Hola! jeje"
        "Has conseguido llegar hasta aquí.\n\n"
        "Aun te falta un paso tienes que descubrir como funciona esto. Es facil solo tienes que descibrir la ultima pista"
        "y es /xyuypi es raro lo see alomejor no esta cifrado pero no te preocupes que el numero de la clave te lo sabes"
    )
    bot.send_message(message.chat.id, mensaje_bienvenida)


@bot.message_handler(commands=['regalo'])
def regalo(message):
    today = datetime.date.today()
    user = message.from_user.id
    key = f"{user}_{today}"
    if key in opened_gifts:
        bot.send_message(message.chat.id, "Lo siento, ya has abierto tu regalo. ¡Tienes que esperar hasta mañana!")
    else:

        frases_regalos = [
            "1.No te habrá sido fácil llegar hasta aquí, esto es lo primero que tengo que decirte, Gracias por ser tú, te quiero.",
            "2.Cada día me enseñas algo nuevo, algo valioso, algo que no cambiaría",
            "3.No demos todo por perdido, mientras quede vida en un latido",
            "4.La magia de la Navidad está en el aire",
            "5.Cada día a tu lado es una aventura",
            "6.El calendario de adviento nos recuerda la importancia de la paciencia y la ilusión",
            "7.Porque soy el fan número uno De esa música que hacen tus tacones Cuando camino a tu lado",
            "8.Hoy es un día especial, vamos a disfrutarlo y que sea inolvidable",
            "9.Se la persona que de alas para volar y raíces para mantenerme fuerte",
            "10.Contigo no me hace falta ni hacer boceto,Sé muy bn lo que quiero,Y lo que quiero es que no seas mi secreto",
            "11.En un mundo lleno de cambios, tú eres mi constante",
            "12.Cuando habla o cuando calla, él lo hace por mandato de su alma, tiene frío pero no acepta bufandas tiene la garganta libre«pa» poder gritar lo que le dé la gana",
            "13.Cada día de adviento es una oportunidad para compartir tu felicidad",
            "14.La verdadera magia de la Navidad reside en compartir momentos especiales",
            "15.Un día más cerca de la Navidad",
            "16.Hoy se que es un día especial para tí jajaja espero no tener mucha resaca para disfrutarlo contigo",
            "17.Contigo, cada día es un nuevo capítulo de un libro que estamos escribiendo",
            "18.No quiero una loca que me vuelva loco solo quiero una loca que me haga parecer que la locura es poco",
            "19.Yo te eché mi brazo al hombro y un brillo de luz de luna iluminaba tus ojos.",
            "20.Cuando las palabras fallan, la música habla.",
            "21.La Navidad es bonita si es contigo",
            "22.Felicita a tu padre jeje ademas es la loteria a ver si me toca y vamos a celebrarlo"
            "23.Ya queda poquitooo jeje es casi tu ultimo mensaje espero que hayas disfutado del camino",
            "24.Feliz noche buena, te amooo. Estamos lejos pero te siento cerca , además feliz 3 mesesss"
        ]

        regalo_dia = frases_regalos[today.day - 1]
        opened_gifts[key] = True
        bot.send_message(message.chat.id, regalo_dia)


bot.polling()
