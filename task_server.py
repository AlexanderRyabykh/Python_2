# Программа сервера для получения приветствия от клиента и отправки ответа
import json
from socket import *
import datetime
import argparse

import client_server.config as cnf
import client_server.log.server_log_config as svr


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


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-a", "--address", type=str, help="server ip (default is 127.0.0.1)", default='127.0.0.1')
    parser.add_argument("-p", "--port", type=int, help="server port number (default is 7777)", default=7777)
    args = parser.parse_args()


    s.bind((args.address, args.port))  # Присваивает порт 8007
    s.listen(5)  # Переходит в режим ожидания запросов;
    # одновременно обслуживает не более
    # 5 запросов.

    while True:
        client, addr = s.accept()

        probe_client(client)

        data = client.recv(cnf.DATA_SIZE)
        print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
        data_dict = json.loads(data)


        if 'action' not in data_dict:
            code = 400
            error = 'action field is required'
            response_msg_str = build_error_for_client(code=code, error=error)
            client.send(response_msg_str.encode('utf-8'))
            client.close()

        action = data_dict['action']
        if action == 'presence':
            svr.logger.info('пользователь в сети')

        # client.close() # нужно ли здесь закрыть клиент-сокет в конце работы?
