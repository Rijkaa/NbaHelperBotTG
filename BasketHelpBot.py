import telebot
import config
import pandas as pd
import imgkit
import os


bot = telebot.TeleBot(config.token)
config = imgkit.config(wkhtmltoimage=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row ('/team')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row ('/Западная', '/Восточная')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row ('/Северо-Западный', '/Тихоокеанский', '/Юго-Западный')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row ('/Антлантический', '/Центральный', '/Юго-Восточный')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row ('Портленд', 'Оклахома', 'Юта', 'Миннесота', 'Денвер')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row ('Голден Стейт', 'ЛА Клипперс', 'ЛА Лейкерс', 'Сакраменто', 'Финикс')
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row ('Хьюстон', 'Нью-Орлеан', 'Сан-Антонио', 'Даллас', 'Мемфис')
keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard8.row ('Торонто', 'Бостон', 'Филадельфия', 'Нью-Йорк', 'Бруклин')
keyboard9 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard9.row ('Кливленд', 'Индиана','Милуоки', 'Детройт', 'Чикаго')
keyboard10 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard10.row ('Майами', 'Вашингтон', 'Шарлотт', 'Орландо', 'Атланта')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, 'Команда /team - после введения названия команды выводит Advanced Statistics для данной команды', reply_markup=keyboard1)


@bot.message_handler(commands=['team'])
def choose_conference(message):
    bot.send_message(message.chat.id, 'Выбери конференцию команды',reply_markup=keyboard2)


@bot.message_handler(commands=['Западная'])
def choose_division1(message):
     bot.send_message(message.chat.id, 'Выбери дивизион', reply_markup=keyboard3)


@bot.message_handler(commands=['Восточная'])
def choose_division2(message):
    bot.send_message(message.chat.id, 'Выбери дивизион', reply_markup=keyboard4)


@bot.message_handler(commands=['Северо-Западный'])
def choose_team1(message):
    bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard5)


@bot.message_handler(commands=['Тихоокеанский'])
def choose_team2(message):
    bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard6)


@bot.message_handler(commands=['Юго-Западный'])
def choose_team3(message):
    bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard7)


@bot.message_handler(commands=['Атлантический'])
def choose_team4(message):
    bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard8)

@bot.message_handler(commands=['Центральный'])
def choose_team5(message):
    bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard9)


@bot.message_handler(commands=['Юго-Восточный'])
def choose_team6(message):
    bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard10)


@bot.message_handler(content_types=['text'])
def team_stats_output(message):
    if message.text == 'Портленд':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/POR/")
    elif message.text == 'Оклахома':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/OKC/")
    elif message.text == 'Юта':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/UTA/")
    elif message.text == 'Денвер':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/DEN/")
    elif message.text == 'Миннесота':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/MIN/")
    elif message.text == 'Голден Стейт':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/GSW/")
    elif message.text == 'ЛА Клипперс':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/LAC/")
    elif message.text == 'ЛА Лейкерс':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/LAL/")
    elif message.text == 'Сакраменто':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/SAC/")
    elif message.text == 'Финикс':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/PHO/")
    elif message.text == 'Хьюстон':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/HOU/")
    elif message.text == 'Сан-Антонио':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/SAS/")
    elif message.text == 'Даллас':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/DAL/")
    elif message.text == 'Мемфис':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/MEM/")
    elif message.text == 'Торонто':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/TOR/")
    elif message.text == 'Бостон':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/BOS/")
    elif message.text == 'Филадельфия':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/PHI/")
    elif message.text == 'Бруклин':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/BRK/")
    elif message.text == 'Нью-Йорк':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/NYK/")
    elif message.text == 'Милуоки':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/MIL/")
    elif message.text == 'Кливленд':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/CLE/")
    elif message.text == 'Индиана':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/IND/")
    elif message.text == 'Детройт':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/DET/")
    elif message.text == 'Чикаго':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/CHI/")
    elif message.text == 'Майами':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/MIA/")
    elif message.text == 'Вашингтон':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/WAS/")
    elif message.text == 'Шарлотт':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/CHO/")
    elif message.text == 'Орландо':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/ORL/")
    elif message.text == 'Атланта':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/ATL/")
    elif message.text == 'Нью-Орлеан':
        tables, = pd.read_html("https://www.basketball-reference.com/teams/NOP/")
    tables.to_csv("tables.csv", index=False)
    data = pd.read_csv(open("tables.csv", "r"))
    text_file = open("data.html", "a")
    text_file.write(data.to_html())
    text_file.close()
    config = imgkit.config(wkhtmltoimage=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe")
    imgkit.from_file("data.html", "out.jpg" ,config=config)
    bot.send_document(message.chat.id, open('out.jpg', 'rb') )
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.html')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tables.csv')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'out.jpg')
    os.remove(path)
    bot.send_message(message.chat.id, 'Чтобы снова выбрать команду, нажми кнопку ниже', reply_markup=keyboard1)


bot.polling()

