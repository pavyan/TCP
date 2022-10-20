import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "localhost"
PORT = 33333

def sendMessage(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, PORT))
            abc = str.encode(text)
            s.sendall(abc)
            data = s.recv(1024)
            notification = bytes.decode(data)
            print(notification)

print("""Введите 1 для ручного ввода сообщения;
Введите 2 для отправки 5 корректных сообщений;
Введите 3 для выхода;
""")



while True:
    a = int(input("Ввод:"))
    if a == 1:
        sendMessage(input('Введите сообщение: '))
    elif a == 2:
        for i in range(5): sendMessage('1234 A1 11:11:11.111 00')
    elif a == 3:
        break


