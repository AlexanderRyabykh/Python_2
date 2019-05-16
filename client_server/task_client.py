# Программа сервера для отправки приветствия сервера и получения ответа
import json
from socket import *
import datetime
import sys
import re

PATTERNS = [re.compile('\d+\.\d+\.\d+\.\d+'),
            re.compile('\d\d\d\d')]

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP

CONFIG = {'addr': None,
          'port': None}

if re.match(PATTERNS[0], sys.argv[1]):
    CONFIG['addr'] = sys.argv[1]
else:
    CONFIG['addr'] = '127.0.0.7'

if re.match(PATTERNS[1], sys.argv[2]):
    CONFIG['port'] = int(sys.argv[2])
else:
    CONFIG['port'] = 8007

s.connect((CONFIG['addr'], CONFIG['port']))   # Соединиться с сервером

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

data_decoded = json.loads(data)
if data_decoded['action'] == 'probe':
    s.send(msg.encode('utf-8'))
    print('Сообщение отправлено')

s.close() # а зачем в клиенте закрывать сокет? скрипт срабатывает и без закрытия