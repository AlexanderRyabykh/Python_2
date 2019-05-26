# Программа сервера для отправки приветствия сервера и получения ответа
import json
from socket import *
import datetime
import argparse

import client_server.config as cnf
import client_server.log.client_log_config as lg



s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-a", "--address", type=str, help="server ip (default is 127.0.0.1)", default='127.0.0.1')
parser.add_argument("-p", "--port", type=int, help="server port number (default is 7777)", default=7777)
args = parser.parse_args()

s.connect((args.address, args.port))   # Соединиться с сервером

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

data = s.recv(cnf.DATA_SIZE)
lg.logger.info('Пришло сообщение от сервера длиной  %s байт', len(data))

data_decoded = json.loads(data)
if data_decoded['action'] == 'probe':
    s.send(msg.encode('utf-8'))
    lg.logger.info('Сообщение %s отправлено', data_decoded['action'])

s.close() # а зачем в клиенте закрывать сокет? скрипт срабатывает и без закрытия