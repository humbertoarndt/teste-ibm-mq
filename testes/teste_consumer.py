# ==============================================================================
# Imports
# ==============================================================================
import unittest
from app.consumer import consumir_mensagem

# ==============================================================================
# Classes
# ==============================================================================
class TestConsumer(unittest.TestCase):
    """
    Classe de teste da função 'consumir_mensagem' do 'consumer'.
    """
    # ==========================================================================
    # Funções
    # ==========================================================================
    def teste_consumir_mensagem(self):
        """
        Testa a função 'consumir_mensagem' para garantir que a função seja executada
        corretamente.

        O teste executa a função 'consumir_mensagem' e verifica se ela não lança
        uma exceção.
        """
        try:
            consumir_mensagem()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)