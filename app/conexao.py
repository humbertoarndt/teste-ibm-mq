# ==============================================================================
# Imports
# ==============================================================================
import pymqi
from .constants import QUEUE_MGR, QUEUE_CHANNEL, conn_string, QUEUE_USER, QUEUE_PSWD
from .logger_config import setup_logger

logger = setup_logger('MQConnection')

# ==============================================================================
# Functions
# ==============================================================================
def conectar_fila():
    """
    Abre conexão com um gerenciador de filas IMB MQ.

    Returns:
        _type_: _description_

    Raises:
        pymqi.MQMIError: Se ocorrer um erro durante a conexão com o IBM MQ.
    """
    try:
        logger.info('Tentando conectar ao Queue Manager...')
        qmgr = pymqi.connect(QUEUE_MGR, QUEUE_CHANNEL, conn_string, QUEUE_USER, QUEUE_PSWD)
        logger.info(f'Conexão estabelecida com o Queue Manager: {QUEUE_MGR}')
        return qmgr
    except pymqi.MQMIError as e:
        logger.info(f'Erro ao conectar ao Queue Manager: {e}')
        raise