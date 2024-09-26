import pymqi
import sys
from .conexao import conectar_fila
from .constants import QUEUE_NAME
from .logger_config import setup_logger

logger = setup_logger('Producer')

def criar_mensagem(mensagem: str) -> None:
    """
    Cria uma nova mensagem e enviar a uma fila IBM MQ.

    Args:
        mensagem (str): A mensagem que será enviada para fila. 

    Raises:
        pymqi.MQMIError: Se ocorrer um erro durante a conexão com o IBM MQ, ou 
        no envio da mensagem a fila.
    """
    try:
        qmgr = conectar_fila()
        fila = pymqi.Queue(qmgr, QUEUE_NAME)
        fila.put(mensagem)
        logger.info(f'Mensagem enviada com sucesso: {mensagem}')
        fila.close()
        fila.disconnect()
        logger.info('Desconectado do Queue Manager.')
    except pymqi.MQMIError as e:
        logger.info(f'Erro ao enviar mensagem: {e}')
        raise


def main():
    """
    Função principal para invocar a criação de uma mensagem.
    """
    if len(sys.argv) != 2:
        print("Uso: python3 -m app.producer <mensagem>")
        sys.exit(1)

    mensagem = sys.argv[1]
    criar_mensagem(mensagem)


if __name__ == '__main__':
    main()