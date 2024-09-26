# ==============================================================================
# Imports
# ==============================================================================
import unittest
from app.conexao import conectar_fila

# ==============================================================================
# Classes
# ==============================================================================
class TestConexao(unittest.TestCase):
    """
    Classe de teste para a função 'conectar_fila' do 'conexao'.
    """
    # ==========================================================================
    # Funções
    # ==========================================================================
    def teste_conexao(self):
        """
        Testa a função 'conectar_fila' para garantir que uma conexão com a gerenciador
        de filas seja estabelecida.

        O teste executa a função 'conectar_fila' e verifica se ela não lança uma
        exceção.
        """
        try:
            conectar_fila()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)