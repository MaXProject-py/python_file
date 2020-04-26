from socket import *
from time import ctime
import os


tcpServ = socket(AF_INET, SOCK_STREAM)  # создание обьекта сокета протакола TCP
tcpServ.bind(('', 21567))  # host, port
tcpServ.listen(5)

while True:
    print('Ожидается подключение...')
    tcpCli, addr = tcpServ.accept()
    print('Соединение  с ', addr)

    while True:
        data = tcpCli.recv(1024)  # размер буфера 1 Кбайт
        udata = data.decode('utf-8')  # декодирование последовательности байтов(bytes) в строку(str)


        if not data:
            print('Соединение разорвано!\n')
            break

        print(udata)
        print('Отправка пакета на ', addr)

        if udata == "os":
            while True:
                tcpCli.send(b'[%s] %s ' % (bytes(os.name, 'utf-8'), udata.encode('utf-8')))
                break

        elif udata == 'ls':     # выводит содержимое каталога
            while True:
                ls_dir = os.listdir(path=".")
                ls = ' '.join(ls_dir)        # Соединение списка в строку
                tcpCli.send(b'%s' % (bytes(ls, 'utf-8')))
                break

        elif udata == 'pwd':
            while True:
                pwd = os.path.abspath(path='.')
                tcpCli.send(b'%s' % (bytes(pwd, 'utf-8')))
                break

        else:
            # кодирование строки и ее отправка с префиксом времени
            tcpCli.send(b'[%s] %s ' % (bytes(ctime(), 'utf-8'), udata.encode('utf-8')))

    tcpCli.close()
