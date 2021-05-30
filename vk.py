from re import A, S
from nltk.util import pr
from nltk.tokenize import word_tokenize
from vk_botting.attachments import Photo
from dick import slovar
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
import vk_botting
import nltk
import httplib2
import apiclient.discovery

bot = vk_botting.Bot('your-prefix-here')
# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1YO96RcOKMHJFA9vjT3L3PjOx-OD3yme15zGlji4ysBQ'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
# Проверка работоспособности 
@bot.listen()
async def on_ready():
    print(f'бот запущен в {bot.group.name}')
    
# Функция проверки слов 
@bot.listen()  #FRONT dev
async def on_message_new(message):
    mssg = message.text
    res=word_tokenize(mssg.lower(), language="russian")
    for j in range(len(slovar)):
        for i in range(len(res)):
            if slovar[j].lower()==res[i] or res[i]=='javascript' or res[i]=='react' or res[i]=='angular' or res[i]=='javascript,' or res[i]=='react,' or res[i]=='angular,':
                answr='Frontend разработчик (стажер):\nhttps://edu.greenatom.ru/trainee/48483/101/\nМожете записаться на стажировку: \nhttps://edu.greenatom.ru/trainee/form/48483/101/' #FRONT dev
                await message.send(answr)
                answr='Обязательно заполните форму: https://docs.google.com/forms/d/e/1FAIpQLSc-1q-VoXDZhceCLEX8BlLiIbPd4aj_a0DGsCC7n_g3H-xR5w/viewform?usp=sf_link'
                await message.send(answr)
        break

# Функция проверки слов 
@bot.listen()  #BACK dev
async def on_message_new(message):
    mssg = message.text
    res=word_tokenize(mssg.lower(), language="russian")
    for j in range(len(slovar)):
        for i in range(len(res)):
            if slovar[j].lower()==res[i] or res[i]=='asp' or res[i]=='sql' or res[i]=='web api' or res[i]=='c' or res[i]=='ms sql' or res[i]=='odata' or res[i]=='soap' or res[i]=='asp,' or res[i]=='sql,' or res[i]=='web api,' or res[i]=='c,' or res[i]=='ms sql,' or res[i]=='odata,' or res[i]=='soap,':
                answr='Backend разработчик (стажер):\nhttps://edu.greenatom.ru/trainee/48485/66/\n Можете записаться на стажировку: https://edu.greenatom.ru/trainee/form/48485/101/'
                await message.send(answr)
                answr='Обязательно заполните форму: https://docs.google.com/forms/d/e/1FAIpQLSc-1q-VoXDZhceCLEX8BlLiIbPd4aj_a0DGsCC7n_g3H-xR5w/viewform?usp=sf_link'
                await message.send(answr)
        break
    
# Функция проверки слов 
@bot.listen() #ADMIN
async def on_message_new(message):
    mssg = message.text
    res=word_tokenize(mssg.lower(), language="russian")
    for j in range(len(slovar)):
        for i in range(len(res)):
            if slovar[j].lower()==res[i] or res[i]=='word' or res[i]=='excel' or res[i]=='powerpoint' or res[i]=='outlook' or res[i]=='студент' or res[i]=='2' or res[i]=='3' or res[i]=='4' or res[i]=='word,' or res[i]=='excel,' or res[i]=='powerpoint,' or res[i]=='outlook,' or res[i]=='студент':
                answr='Администратор IT-проектов (стажер): \nhttps://edu.greenatom.ru/trainee/48738/101/\n Можете записаться на стажировку:\nhttps://edu.greenatom.ru/trainee/form/48738/101/' #ADMIN
                await message.send(answr)
                answr='Обязательно заполните форму: https://docs.google.com/forms/d/e/1FAIpQLSc-1q-VoXDZhceCLEX8BlLiIbPd4aj_a0DGsCC7n_g3H-xR5w/viewform?usp=sf_link'
                await message.send(answr)
        break 
    
# Функция проверки слов 
@bot.listen() #Dataspec +
async def on_message_new(message):
    mssg = message.text
    res=word_tokenize(mssg.lower(), language="russian")
    for j in range(len(slovar)):
        for i in range(len(res)):
            if slovar[j].lower()==res[i] or res[i]=='пк' or res[i]=='студент' or res[i]=='1' or res[i]=='2' or res[i]=='интернет' or res[i]=='общительность' or res[i]=='общительная' or res[i]=='общительный' or res[i]=='коммуникабельость' or res[i]=='коммуникабельный' or res[i]=='пк' or res[i]=='студент' or res[i]=='1' or res[i]=='2' or res[i]=='интернет' or res[i]=='общительность,' or res[i]=='общительная,' or res[i]=='общительный,' or res[i]=='коммуникабельость,' or res[i]=='коммуникабельный,':
                answr='Специалист по разметке данных (стажер):\nhttps://edu.greenatom.ru/trainee/48770/101/  \nМенеджер услуги (стажер): \nhttps://edu.greenatom.ru/trainee/48765/101/' #ADMIN 
                await message.send(answr)
                answr='Обязательно заполните форму: https://docs.google.com/forms/d/e/1FAIpQLSc-1q-VoXDZhceCLEX8BlLiIbPd4aj_a0DGsCC7n_g3H-xR5w/viewform?usp=sf_link'
                await message.send(answr)
        break 

# Функция проверки слов 
@bot.listen() #it struckt +
async def on_message_new(message):
    mssg = message.text
    res=word_tokenize(mssg.lower(), language="russian")
    for j in range(len(slovar)):
        for i in range(len(res)):
            if slovar[j].lower()==res[i] or res[i]=='c++' or res[i]=='#' or res[i]=='python' or res[i]=='java' or res[i]=='nix' or res[i]=='cmd' or res[i]=='админ' or res[i]=='командная' or res[i]=='админство':
                answr='Специалист по разметке данных (стажер):\nhttps://edu.greenatom.ru/trainee/48770/101/\n Можете записаться на стажировку:\nhttps://edu.greenatom.ru/trainee/form/48770/101/' #ADMIN 
                await message.send(answr)
                answr='Обязательно заполните форму: https://docs.google.com/forms/d/e/1FAIpQLSc-1q-VoXDZhceCLEX8BlLiIbPd4aj_a0DGsCC7n_g3H-xR5w/viewform?usp=sf_link'
                await message.send(answr)
        break 

bot.run('a88c48763a5cf5a04c2d215eea274b38f4692368924c2a1789b69ada12d25296144511f4ed3eeeb1bbc02')        
             
             
             
             
        