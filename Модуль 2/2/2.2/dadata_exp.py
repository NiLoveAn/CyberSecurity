from pprint import pprint
from dadata import Dadata
token = "---"
secret = "---"
dadata = Dadata(token, secret)
result = dadata.clean("address", "мск сухонска 11/-89")
print(result, '\n')
# pprint(result)


# импортируем библиотеку dadata
# добавляем токен (из личного кабинета сайта)
# добавляем включ (из ЛК)
# сообщаем свои токен и ключ для обращения
# просим подробный адрес для “спб невский 10”
# выводим результат в консоль