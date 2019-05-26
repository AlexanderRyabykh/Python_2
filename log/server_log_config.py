import logging

logging.basicConfig(filename='log\\server.log',
                    format='%(asctime)s %(levelname)-10s %(module)s %(message)s',
                    level=logging.INFO)

logger = logging.getLogger('server')

server_log = logging.FileHandler('log\\server.log', encoding='utf-8')
server_log.setLevel(logging.INFO)

logger.addHandler(server_log)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    pass
