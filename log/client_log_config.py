import logging

logging.basicConfig(filename='log\\client.log',
                    format='%(asctime)s %(levelname)-10s %(module)s %(message)s',
                    level=logging.INFO)

logger = logging.getLogger('client')

client_log = logging.FileHandler('log\\client.log', encoding='utf-8')
client_log.setLevel(logging.INFO)

logger.addHandler(client_log)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    pass
