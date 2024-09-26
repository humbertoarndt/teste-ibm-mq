import pymqi
import sys
from .constants import *

try:
    print('Conectando ao Queue Manager...')
    qmgr = pymqi.connect(QUEUE_MGR, QUEUE_CHANNEL, conn_string, QUEUE_USER, QUEUE_PSWD)
    if qmgr:
        print(f'Conexão estabelecida com o Queue Manager: {QUEUE_MGR}')
    queue = pymqi.Queue(qmgr, QUEUE_NAME)
    message = "Humberto, Doisberto, Trêsberto"
    queue.put(message)
    print(f'Mensagem enviada com sucesso: {message}')
    queue.close()
    qmgr.disconnect()  
    print('Desconectado do Queue Manager.')
except pymqi.MQMIError as e:
    print(f'Erro: {e}')
    sys.exit(1)
