import requests

url = 'https://www.tulasamovar.ru/'
response = requests.get(url)
response.raise_for_status()

print(response.text)