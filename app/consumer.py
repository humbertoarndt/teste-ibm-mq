# ==============================================================================
# Imports
# ==============================================================================
import pymqi
from .conexao import conectar_fila
from .constants import QUEUE_NAME
from .logger_config import setup_logger

logger = setup_logger('Consumer')

# ==============================================================================
# Functions
# ==============================================================================
def consumir_mensagem():
    """
    Consume a primeira mensagem em uma fila IBM MQ.

    Raises:
        pymqi.MQMIError: Se ocorrer um erro durante a conexão com o IBM MQ, ou 
        no consumo da mensagem em fila.
    """
    try:
        qmgr = conectar_fila()
        fila = pymqi.Queue(qmgr, QUEUE_NAME)
        mensagem = fila.get()
        logger.info(f'Mensagem recebida: {mensagem.decode("utf-8")}')
        fila.close()
        fila.desconnect()
        logger.info('Desconectado do Queue Manager.')
    except pymqi.MQMIError as e:
        logger.info(f'Erro ao consumir mensagem: {e}')
        raise


def main():
    """
    Função principal para invocar o consumo de uma mensagem.
    """
    consumir_mensagem()


if __name__ == '__main__':
    main()