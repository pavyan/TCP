import re
from datetime import datetime

class Message:
    def __init__(self, recievedMessage):
        self.initialMessage = recievedMessage
        self.number = recievedMessage[0:4]
        self.channelId = recievedMessage[5:7]
        self.time = recievedMessage[8:18]
        self.group = recievedMessage[21:23]
            
class Messenger:
    
    def read(self, inputMessage):
        matcher = re.compile(r"^\d{4}\ \w{2}\ \d{2}\:\d{2}\:\d{2}\.\d{3}\ \d{2}$")
        if not re.match(matcher, inputMessage):
            print('Неверный формат сообщения, попробуйте снова')
            messageForLog = 'Неверный формат сообщения'
            return([messageForLog])
        else:
            msg = Message(inputMessage)
            messageForWrite = f'Спортсмен, нагрудный номер {msg.number} прошел отсечку {msg.channelId} в {msg.time}'
            messageForLog = inputMessage
            return(messageForWrite, messageForLog)
                
    def write(self, msg, condition):
        if int(Message(condition).group) == 00:
                print(msg)

    def log(self, msg):
        with open('log.log', 'a') as file:
            file.write(f'{datetime.now()}  Сообщение: {msg}\n')
        return(msg)