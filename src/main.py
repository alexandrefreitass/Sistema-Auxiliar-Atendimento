"""
Ponto de entrada principal do aplicativo.
"""

import sys
import os

# Adicionar o diretório pai ao Python path para importações
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gui.main_window import MainWindow
from src import __version__


def main():
    """Função principal do aplicativo."""
    print(f"Iniciando Aplicativo de Auxílio ao Atendimento 190 v{__version__}")
    
    try:
        # Criar e exibir a janela principal
        app = MainWindow()
        app.show()
        
    except Exception as e:
        print(f"Erro fatal ao iniciar aplicativo: {e}")
        import FreeSimpleGUI as sg
        sg.popup_error(
            f"Erro fatal ao iniciar o aplicativo:\n{str(e)}",
            title="Erro Fatal"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()