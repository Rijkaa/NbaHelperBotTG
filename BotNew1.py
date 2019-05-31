import telebot
import config
import pandas as pd
import imgkit
import os
from PIL import Image
from pathlib import Path


bot = telebot.TeleBot(config.token)
config = imgkit.config(wkhtmltoimage=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/team')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Западная', 'Восточная')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Северо-Западный', 'Тихоокеанский')
keyboard3.row('Юго-Западный')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Атлантический', 'Центральный')
keyboard4.row('Юго-Восточный')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('Портленд', 'Оклахома', 'Юта')
keyboard5.row('Миннесота', 'Денвер')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Голден Стейт', 'ЛА Клипперс', 'ЛА Лейкерс')
keyboard6.row('Сакраменто', 'Финикс')
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('Хьюстон', 'Нью-Орлеан', 'Сан-Антонио')
keyboard7.row('Даллас', 'Мемфис')
keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard8.row('Торонто', 'Бостон', 'Филадельфия')
keyboard8.row('Нью-Йорк', 'Бруклин')
keyboard9 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard9.row('Кливленд', 'Индиана','Милуоки')
keyboard9.row('Детройт', 'Чикаго')
keyboard10 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard10.row('Майами', 'Вашингтон', 'Шарлотт')
keyboard10.row('Орландо', 'Атланта')
keyboard11 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard11.row('/team')
keyboard11.row('Броски', 'Scoring', 'Подборы')
keyboard11.row('Блоки', 'Перехваты', 'Потери', 'Фолы')
keyboard11.row('Game log')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, 'Команда /team - после введения названия команды выводит Advanced Statistics для данной команды, или можешь ввести имя и фамилию игрока на английском языке, и я выведу его статистику за этот сезон', reply_markup=keyboard1)


@bot.message_handler(commands=['team'])
def choose_conference(message):
    bot.send_message(message.chat.id, 'Выбери конференцию команды',reply_markup=keyboard2)


@bot.message_handler(content_types=['text'])
def team_stats_output(message):
    k = message.text
    global site_ad
    global widthtype
    par = 0
    if message.text == 'Западная':
        bot.send_message(message.chat.id, 'Выбери дивизион', reply_markup=keyboard3)
        par = 1
    elif message.text == 'Восточная':
        bot.send_message(message.chat.id, 'Выбери дивизион', reply_markup=keyboard4)
        par = 1
    elif message.text == 'Северо-Западный':
        bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard5)
        par = 1
    elif message.text == 'Тихоокеанский':
        bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard6)
        par = 1
    elif message.text == 'Юго-Западный':
        bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard7)
        par = 1
    elif message.text == 'Атлантический':
        bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard8)
        par = 1
    elif message.text == 'Центральный':
        bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard9)
        par = 1
    elif message.text == 'Юго-Восточный':
        bot.send_message(message.chat.id, 'Выбери команду', reply_markup=keyboard10)
        par = 1
    elif message.text == 'Портленд':
        site_ad = 'https://www.teamrankings.com/nba/team/portland-trail-blazers/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Оклахома':
        site_ad = "https://www.teamrankings.com/nba/team/oklahoma-city-thunder/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Юта':
        site_ad = 'https://www.teamrankings.com/nba/team/utah-jazz/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Денвер':
        site_ad = "https://www.teamrankings.com/nba/team/denver-nuggets/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Миннесота':
        site_ad = 'https://www.teamrankings.com/nba/team/minnesota-timberwolves/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Голден Стейт':
        site_ad = "https://www.teamrankings.com/nba/team/golden-state-warriors/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'ЛА Клипперс':
        site_ad = "https://www.teamrankings.com/nba/team/la-clippers/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'ЛА Лейкерс':
        site_ad = "https://www.teamrankings.com/nba/team/la-lakers/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Сакраменто':
        site_ad = 'https://www.teamrankings.com/nba/team/sacramento-kings/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Финикс':
        site_ad = 'https://www.teamrankings.com/nba/team/phoenix-suns/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Хьюстон':
        site_ad = "https://www.teamrankings.com/nba/team/houston-rockets/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Сан-Антонио':
        site_ad = 'https://www.teamrankings.com/nba/team/san-antonio-spurs/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Даллас':
        site_ad = "https://www.teamrankings.com/nba/team/dallas-mavericks/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Мемфис':
        site_ad = "https://www.teamrankings.com/nba/team/memphis-grizzlies/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Торонто':
        stat = 'Points/Game'
        widthtype = 520
        site_ad = 'https://www.teamrankings.com/nba/team/toronto-raptors/stats'
    elif message.text == 'Бостон':
        site_ad = 'https://www.teamrankings.com/nba/team/boston-celtics/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Филадельфия':
        site_ad = 'https://www.teamrankings.com/nba/team/philadelphia-76ers/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Бруклин':
        stat = 'Points/Game'
        widthtype = 520
        site_ad = "https://www.teamrankings.com/nba/team/brooklyn-nets/stats"
    elif message.text == 'Нью-Йорк':
        stat = 'Points/Game'
        widthtype = 520
        site_ad = "https://www.teamrankings.com/nba/team/new-york-knicks/stats"
    elif message.text == 'Милуоки':
        site_ad = "https://www.teamrankings.com/nba/team/milwaukee-bucks/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Кливленд':
        stat = 'Points/Game'
        widthtype = 520
        site_ad = "https://www.teamrankings.com/nba/team/cleveland-cavaliers/stats"
    elif message.text == 'Индиана':
        site_ad = "https://www.teamrankings.com/nba/team/indiana-pacers/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Детройт':
        site_ad = "https://www.teamrankings.com/nba/team/detroit-pistons/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Чикаго':
        stat = 'Points/Game'
        widthtype = 520
        site_ad = "https://www.teamrankings.com/nba/team/chicago-bulls/stats"
    elif message.text == 'Майами':
        site_ad = "https://www.teamrankings.com/nba/team/miami-heat/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Вашингтон':
        site_ad = 'https://www.teamrankings.com/nba/team/washington-wizards/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Шарлотт':
        site_ad = "https://www.teamrankings.com/nba/team/charlotte-hornets/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Орландо':
        site_ad = "https://www.teamrankings.com/nba/team/orlando-magic/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Атланта':
        site_ad = "https://www.teamrankings.com/nba/team/atlanta-hawks/stats"
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Нью-Орлеан':
        site_ad = 'https://www.teamrankings.com/nba/team/new-orleans-pelicans/stats'
        stat = 'Points/Game'
        widthtype = 520
    elif message.text == 'Броски':
        stat = 'Effective FG %'
        widthtype = 520
    elif message.text == 'Scoring':
        stat = '1st Qtr Pts/Gm'
        widthtype = 528
    elif message.text == 'Подборы':
        stat = 'Off Rebounds/Gm'
        widthtype = 528
    elif message.text == 'Блоки':
        stat = 'Blocks/Game'
        widthtype = 574
    elif message.text == 'Перехваты':
        stat ='Steals/Game'
        widthtype = 579
    elif message.text == 'Потери':
        stat = 'Turnovers/Game'
        widthtype = 550
    elif message.text == 'Фолы':
        stat ='Personal Fouls/Gm'
        widthtype = 517
    elif message.text == 'Game log':
        site_ad = site_ad.replace('stats', 'game-log')
        stat = 'Date'
        widthtype = 634
    elif isinstance(k, str):
        k = k.replace(' ', '-')
        stat = 'Stat'
        widthtype = 322
        k.lower()
        site_ad = 'https://www.teamrankings.com/nba/player/' + k + '/stats'
    if par == 0:
        bot.send_message(message.chat.id, 'Подожди, идёт обработка запроса')
        tables, = pd.read_html(site_ad, match=stat, header=0)
        tables.to_csv("tables.csv", index=False)
        data = pd.read_csv(open("tables.csv", "r"))
        text_file = open("data.html", "a")
        text_file.write(data.to_html())
        text_file.close()
        config = imgkit.config(wkhtmltoimage=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe")
        imgkit.from_file("data.html", "out.jpg" ,config=config)
        imgfile = Path('out.jpg')
        img = Image.open(imgfile)
        width = img.size[0] - widthtype
        height = img.size[1]
        img3 = img.crop((0,0,width,height))
        img3.save('out.jpg')
        del widthtype
        bot.send_document(message.chat.id, open('out.jpg', 'rb') )
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.html')
        os.remove(path)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tables.csv')
        os.remove(path)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'out.jpg')
        os.remove(path)
        if (stat != 'Stat'):
            bot.send_message(message.chat.id, 'Чтобы снова выбрать команду нажми кнопку ниже. Чтобы узнать статистику по различным параметрам или посмотреть гейм лог команды, выбери одину из кнопок предложенных ниже. Чтобы узнать статистику какого-либо игрока напиши мне его имя и фамилию на английском языке', reply_markup=keyboard11)
        else:
            bot.send_message(message.chat.id, 'Чтобы снова выбрать команду нажми кнопку ниже. Чтобы узнать статистику какого-либо игрока напиши мне его имя и фамилию на английском языке', reply_markup=keyboard1)


bot.polling()
