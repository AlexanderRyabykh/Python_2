# Программа сервера для получения приветствия от клиента и отправки ответа
import json
from socket import *
import datetime

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8007))                # Присваивает порт 8007
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
    probe_msg = {
        "action": "probe",
        "time": str(datetime.datetime.utcnow()),
    }
    client.send(probe_msg.encode('utf-8'))
    client.close()


while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)

    data_dict = json.loads(data)

    if 'action' not in data_dict:
        code = 400
        error = 'action field is required'
        response_msg_str = build_error_for_client(code=code, error=error)
        client.send(response_msg_str.encode('utf-8'))
        client.close()

    probe_client(client)
    action = data_dict['action']

    if action == 'presence':
        print('пользователь в сети')


