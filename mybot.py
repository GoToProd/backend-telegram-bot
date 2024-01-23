import telebot
from telebot import types

bot = telebot.TeleBot("2132151577:AAGRlXdWag2rCbZdeT5puz9YKKx4Bz0NUpE")
admin = 1110147997
print('Запустился')

name = ''
surname = ''
age = 0
proecty = ''
zarplata = ''
obrSvyaz = ''


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я HR-It бот, если ты готов пройти собеседование, напиши /go")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Данный бот предназначен для оставления резюме <<Боссу>>.\n "
                          "Для того что бы войти в главное меню нажми /start\n"
                          "Для того что бы начать проходить собеседование нажми /go")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, "Привет, я HR-It бот, если ты готов пройти собеседование, напиши /go\n"
                              "Справка - /help")
    elif message.text == 'Hi':
        bot.reply_to(message, "Hi, I`am HR-It bot and if you ready start - write /go\n"
                              "For help - /help")
    elif message.text == '/go':
        bot.send_message(message.from_user.id, "Отлично.\nНачнем:\n (6/1) - Ваше имя?")
        bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "(6/2) - Ваша фамилия?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "(6/3) - Ваш Возраст?")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Введите возраст цифрами.")
            break
    if age == 0:
        bot.register_next_step_handler(message, reg_age)
    else:
        bot.send_message(message.from_user.id, "(6/4) - В каких проектах участвовали и на чем вы кодите?")
        bot.register_next_step_handler(message, reg_proecty)

def reg_proecty(message):
    global proecty
    proecty = message.text
    bot.send_message(message.from_user.id, "(6/5) - Какую заработную плату вы хотели бы получать?")
    bot.register_next_step_handler(message, reg_zarplata)

def reg_zarplata(message):
    global zarplata
    zarplata = message.text
    bot.send_message(message.from_user.id, "(6/6) - Оставьте ваши контактные данные для обратной связи.")
    bot.register_next_step_handler(message, reg_obrSvyaz)

def reg_obrSvyaz(message):
    global obrSvyaz
    obrSvyaz = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
    keyboard.add(key_no)
    questions = "Твой возраст - " + str(age) + " лет и тебя зовут: " + name + " " + surname + ", участвовал в проектах и кодишь: "+ proecty +", желаемая зарплата - "+ zarplata +", обратная связь - "+ obrSvyaz +". Все верно?"
    bot.send_message(message.from_user.id, text = questions, reply_markup=keyboard)
    bot.send_message(1110147997, text="Новый пользователь -" + name + " " + surname + ",\n возраст - " + str(
        age) + ",\n проекты и кодинг: " + proecty + "\n Желаемая зарплата" + zarplata + "\n обратная связь" + obrSvyaz + "")

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Отлично, ваше резюме отправлено <<Боссу>>, ожидайте обратной связи!")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Окей, попробуй еще раз.")
        name = ''
        surname = ''
        age = 0
        projets = ''
        zarplata = ''
        obrSvyaz = ''
        bot.send_message(call.message.chat.id, "(6/1) - Ваше имя?")
        bot.register_next_step_handler(call.message, reg_name)








bot.polling()
