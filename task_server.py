# Программа сервера для получения приветствия от клиента и отправки ответа
import json
from socket import *
import datetime
import sys
import re

PATTERNS = [re.compile('\d+\.\d+\.\d+\.\d+'),
            re.compile('\d\d\d\d')]

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP

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

s.bind((CONFIG['addr'], CONFIG['port']))                # Присваивает порт 8007
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # одновременно обслуживает не более
                                  # 5 запросов.


def build_error_for_client(code, error):
    response_msg = {
        'response': code,
        'error': error
    }
    response_msg_str = json.dumps(response_msg)
    return response_msg_str


def probe_client(client):
    probe = {
        'action': 'probe',
        'time': str(datetime.datetime.utcnow()),
    }
    probe_msg = json.dumps(probe)
    client.send(probe_msg.encode('utf-8'))
    # client.close() # если закрываю клиент здесь, сервер перестанет работать


while True:
    client, addr = s.accept()


    probe_client(client)

    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    data_dict = json.loads(data)
    action = data_dict['action']

    if 'action' not in data_dict:
        code = 400
        error = 'action field is required'
        response_msg_str = build_error_for_client(code=code, error=error)
        client.send(response_msg_str.encode('utf-8'))
        client.close()

    if action == 'presence':
        print('пользователь в сети')

    # client.close() # нужно ли здесь закрыть клиент-сокет в конце работы?
