import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com']:
    try:
        response = requests.get(url)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print(response.headers)
        #Свойство позволяет просмотреть заголовки ответа сервера: его тип, дату обращения, формат содержимого, кодировку и др.
        print(response.status_code)
        #Код статуса 200 говорит о том, что запрашиваемый сайт обнаружен, и мы от него получили успешный ответ.
        print(response.text)
        print(response.json())
        #Свойство text показывает тело ответа сервера в текстовом формате (актуально для html-страниц),
        # content – результат в виде байтов (удобно при скачивании графической, аудио- или видеоинформации),
        # метод json() приводит содержимое ответа к обычному словарю (если данные к нему приводимы,
        # в противном случае будет ошибка, как в примере; актуально для API-запросов).
