# ==============================================================================
# Imports
# ==============================================================================
import unittest
from app.producer import criar_mensagem

# ==============================================================================
# Classes
# ==============================================================================
class TestProducer(unittest.TestCase):
    """
    Classe de testes da função 'criar_mensagem' do 'producer'.
    """
    # ==========================================================================
    # Funções
    # ==========================================================================
    def teste_criar_mensagem(self):
        """
        Testa a função 'criar_mensagem' para garantir que função seja executada
        corretamente.

        O teste executa a função 'criar_mensagem' e verifica se ela não lança uma
        exceção.
        """
        mensagem = "Humberto Doisberto"
        try:
            criar_mensagem(mensagem)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)