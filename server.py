from socketserver import *
import message_handler as mh
from threading import Thread

messenger = mh.Messenger()

host = 'localhost'
port = 33333
addr = (host,port)

class MessageHandler(StreamRequestHandler):
    
    def handle(self):     
        self.data = self.request.recv(1024)

        readReturn = messenger.read(bytes.decode(self.data))

        if len(readReturn) == 1:
            messageForLog = readReturn[0]
            messenger.log(messageForLog)

            respond = str.encode('Был отправлен неверный формат сообщения.')
            self.request.sendall(respond)
        else:
            messageForWrite = readReturn[0]
            messageForLog = readReturn[1]
            messenger.log(messageForLog)
            messenger.write(messageForWrite, messageForLog)

            respond = str.encode('Сообщение получено.')
            self.request.sendall(respond)

server = TCPServer(addr, MessageHandler)

def startServer():
    print('Сервер запущен')
    server.serve_forever()

def stopServer():
    server.shutdown()
   
print("Введите 1 для запуска сервера, 2 для остановки")

while True: 
    opt = int(input())
    if opt == 1:
        th = Thread(target=startServer)
        th.start()
    elif opt == 2:
        stopServer()
        break