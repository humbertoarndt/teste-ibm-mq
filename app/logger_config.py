# ==============================================================================
# Imports
# ==============================================================================
import logging

# ==============================================================================
# Functions
# ==============================================================================
def setup_logger(name: str) -> logging.Logger:
    """
    Configura e retorna um logger de saída padrão.

    Args:
        name (str): O nome do logger que será criado.

    Returns:
        logging.Logger: O logger configurado.
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger