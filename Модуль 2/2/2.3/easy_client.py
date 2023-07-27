import socket
# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаемся к серверу
client_socket.connect(('localhost', 12345))
# Отправляем данные серверу
x = input("Your message: ")
client_socket.sendall(x.encode())
# Закрываем соединение
client_socket.close()