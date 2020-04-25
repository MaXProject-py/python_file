from socket import *


tcpCli = socket(AF_INET, SOCK_STREAM)  # создание объекта сокета клиента
tcpCli.connect(('localhost', 21567))   # подключение к серверу

while True:
    data = input('> ')
    if not data:
        break
    tcpCli.send(data.encode('utf-8'))   # запрос на сервер
    data = tcpCli.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))     # вывод сообщения с отрезком времени
tcpCli.close()
