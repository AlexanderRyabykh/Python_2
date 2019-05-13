# Программа сервера для отправки приветствия сервера и получения ответа
import json
from socket import *
import datetime

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 8007))   # Соединиться с сервером
message_dict = {
        "action": "presence",
        "time": str(datetime.datetime.utcnow()),
        "type": "status",
        "user": {
                "account_name":  "C0deMaver1ck",
                "status":      "Yep, I am here!"
        }
}

msg = json.dumps(message_dict)

data = s.recv(100000000)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
if data['action'] == 'probe':
    s.send(msg.encode('utf-8'))
    print('Сообщение отправлено')
s.close()