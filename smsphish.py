# -*- coding: utf8 -*- 
import os
from twilio.twiml.voice_response import Gather, VoiceResponse
from twilio.rest import Client
sampleqiwisite=f'''Здравствуйте, на вашем аккаунте была замечена аномальная активность со стороннего андроид устройства, ваши счета могут быть заморожены. Для разморозки требуется войти в аккаунт и подать заявку на (ваш сайт)'''
sampleqiwiphone=f'''Здравствуйте, на вашем аккаунте была замечена аномальная активность со стороннего андроид устройства, ваши счета могут быть заморожены. Для подтверждение сообщите нашему оператору, который наберет с номера указаного в нижней части страницы https://qiwi.com/support/ код подтверждения'''
def sms(text):
	client = Client(account_sid, auth_token)
	message = client.messages.create(body=text, from_=senderid, to=reciever)
account_sid = input('СИД АККАУНТА:')
auth_token = input('ТОКЕН:')
reciever = input('ПОЛУЧАТЕЛЬ:')
phone= input('ТЕЛЕФОН(можно не вводить если фишинг идет через сайт): ')
senderid=input('Введите имя отправителя: ')
print("Пожалуйста, выберите дейсвтие:")
print("1. Отправить SMS")
print("2. Запросить звонок")
choise = input("Ваш выбор: ")
if (choise == "1"):
	print("Вы хотите использовать шаблон для фишинга киви(1), или желаете написать свое сообщение?(2)")
	bodychoise = input("Ваш выбор: ")
	if (bodychoise == "1"):
		print(f'''1. Фишинг с помощью сайта: \n {sampleqiwisite}''')
		print(f'''2. Фишинг с помлщью телефонного бота: \n {sampleqiwiphone}''')
		samplechoise = input("Ваш выбор: ")
		if (samplechoise == "1"):
			site = input("Введите адресс своего сайта: ")
			text=sampleqiwisite.replace("(ваш сайт)", site)
		elif (samplechoise == "2"):
			text=sampleqiwiphone
	if (bodychoise == "2"):
		text =input("Ваш текст: ")
	print("Пробую послать сообщение...")
	try:
		sms(text)
		print('Сообщение успешно отправлено!')
	except Exception as e:
		print("Неудача, произошла следующая ошибка:")
		print(e)
if (choise == "2"):
	textphising=input('Текст который скажет бот: ')
	langphish=input('Выберите язык: 1. RU, 2.EN: ')
	if (langphish=="1"):
		lang=f'''language="ru-RU"'''
	else:
		lang=f'''language="en-EN"'''
	xml=f'''
<Response>
    <Gather action="https://google.com" method="GET">
        <Say language="ru-RU">
            {textphising}
        </Say>
    </Gather>
    <Say>Error</Say>
</Response>'''
	try:
		client = Client(account_sid, auth_token)
		call = client.calls.create(
                        		twiml=xml,
                        		to=reciever,
                        		from_=phone
                    		)
		print("Успешно!")
	except Exception as e:
		print("Неудача, произошла следующая ошибка:")
		print(e)