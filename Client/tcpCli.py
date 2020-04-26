from socket import *
import argparse
import sys

def createParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('-p', '--port', type=int, default=21567)
    return parser

tcpCli = socket(AF_INET, SOCK_STREAM)

if __name__ == '__main__':
    parser = createParse()
    namespase = parser.parse_args(sys.argv[1:])
    if namespase.host or namespase.port:
        tcpCli.connect((namespase.host, namespase.port))

    print(namespase)

    while True:
        data = input('> ')
        if not data:
            break
        tcpCli.send(data.encode('utf-8'))
        data = tcpCli.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
    tcpCli.close()
