import pymqi
import sys
from .constants import *

try:
    print('Conectando ao Queue Manager...')
    qmgr = pymqi.connect(QUEUE_MGR, QUEUE_CHANNEL, conn_string, QUEUE_USER, QUEUE_PSWD)
    if qmgr:
        print(f'Conexão estabelecida com o Queue Manager: {QUEUE_MGR}')
    queue = pymqi.Queue(qmgr, QUEUE_NAME)
    message = queue.get()
    print(f"Mensagem recebida: {message.decode('utf-8')}")
    queue.close()
    queue.disconnect()
except pymqi.MQMIError as e:
    print(f'Erro: {e}')
    sys.exit(1)