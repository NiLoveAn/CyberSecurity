import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9897))
flag=True
while flag:
    client.send(input('Client_1:').encode('utf-8'))
    message=client.recv(1024).decode('utf-8')
    if message=='quit':
        flag=False
    else:
        print(message)

client.close()