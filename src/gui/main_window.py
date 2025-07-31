"""
Janela principal do aplicativo - Design Moderno
"""

import FreeSimpleGUI as sg

from ..config.settings import (
    TEMA_PADRAO, BUTTON_CONFIGS, TITLE_CONFIG, SUBTITLE_CONFIG,
    MAIN_WINDOW_SIZE, MAIN_WINDOW_TITLE, MAIN_WINDOW_CONFIG,
    FONT_PADRAO, COLORS, BUTTON_TEXTS
)
from ..utils.helpers import open_url, validate_assets

from .secondary_windows import SecondaryWindowManager


class MainWindow:
    """Classe responsável pela janela principal do aplicativo com design moderno."""
    
    def __init__(self):
        """Inicializa a janela principal."""
        self.window = None
        self.secondary_manager = None
        self._setup_theme()
        self._validate_setup()
    
    def _setup_theme(self):
        """Configura o tema moderno da interface."""
        # Usar tema pré-definido como base
        sg.theme('Dark')
    
    def _validate_setup(self):
        """Valida se os assets necessários estão disponíveis."""
        if not validate_assets():
            sg.popup_error(
                "❌ Erro: Alguns arquivos de recursos não foram encontrados.\n\n"
                "🔍 Verifique se a pasta 'assets' está presente e contém todos os arquivos necessários.\n\n"
                "📁 Arquivos necessários:\n"
                "• Imagens de rodovias (rodovia1.png - rodovia6.png)\n"
                "• Imagens de referência (cong.png, telefones.png, ramais.png)\n"
                "• Ícone da aplicação (icon.ico)",
                title="⚠️ Erro de Configuração"
            )
    
    def create_layout(self) -> list:
        """
        Cria o layout moderno da janela principal.
        
        Returns:
            Layout da janela com design atualizado
        """
        return [
            # Cabeçalho com título principal
            [sg.Text('🚨 APOIO 190', **TITLE_CONFIG)],
            [sg.Text('Sistema de Suporte Operacional', **SUBTITLE_CONFIG)],
            
            # Separador visual
            [sg.HorizontalSeparator(pad=((50, 50), (10, 20)))],
            
            # Seção Cartografia
            [sg.Text('📍 RECURSOS CARTOGRÁFICOS', 
                    font=('Segoe UI', 14, 'bold'), 
                    pad=((0, 0), (15, 10)))],
            [
                sg.Button(BUTTON_TEXTS['nota'], key="nota", **BUTTON_CONFIGS['primary']),
                sg.Button(BUTTON_TEXTS['mapa'], key="mapa", **BUTTON_CONFIGS['primary'])
            ],
            [
                sg.Button(BUTTON_TEXTS['rodovia'], key="rodovia", **BUTTON_CONFIGS['primary']),
            ],
            
            # Separador
            [sg.Text('')],  # Espaçamento
            
            # Seção Comunicação
            [sg.Text('📞 COMUNICAÇÃO', 
                    font=('Segoe UI', 14, 'bold'), 
                    pad=((0, 0), (15, 10)))],
            [
                sg.Button(BUTTON_TEXTS['ramais'], key="ramais", **BUTTON_CONFIGS['secondary']),
                sg.Button(BUTTON_TEXTS['telefones'], key="telefones", **BUTTON_CONFIGS['secondary'])
            ],
            
            # Separador
            [sg.Text('')],  # Espaçamento
            
            # Seção Sistemas
            [sg.Text('💻 SISTEMAS CORPORATIVOS', 
                    font=('Segoe UI', 14, 'bold'), 
                    pad=((0, 0), (15, 10)))],
            [
                sg.Button(BUTTON_TEXTS['rancho'], key="rancho", **BUTTON_CONFIGS['primary']),
                sg.Button(BUTTON_TEXTS['sisbol'], key="sisbol", **BUTTON_CONFIGS['primary'])
            ],
            [
                sg.Button(BUTTON_TEXTS['dejem'], key="dejem", **BUTTON_CONFIGS['primary']),
            ],
            
            # Rodapé
            [sg.Text('')],  # Espaçamento
            [sg.HorizontalSeparator(pad=((50, 50), (20, 10)))],
            [sg.Text('Desenvolvido para operadores do 190 | PM-SP', 
                    font=('Segoe UI', 9, 'italic'), 
                    justification='center',
                    pad=((0, 0), (10, 10)))]
        ]
    
    def show(self):
        """Exibe a janela principal moderna e gerencia os eventos."""
        self.secondary_manager = SecondaryWindowManager(self.show)
        
        layout = self.create_layout()
        self.window = sg.Window(
            MAIN_WINDOW_TITLE,
            layout,
            size=MAIN_WINDOW_SIZE,
            element_justification='c',
            finalize=True,
            font=FONT_PADRAO,
            **MAIN_WINDOW_CONFIG,
            resizable=False,
            return_keyboard_events=True,
            use_default_focus=False,
            icon=None  # Pode adicionar ícone personalizado aqui
        )
        
        self._handle_events()
    
    def _handle_events(self):
        """Gerencia os eventos da janela principal."""
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break
            elif event in ['nota', 'telefones', 'ramais', 'rodovia']:
                self._handle_secondary_window(event)
                break  # Evita múltiplas janelas após retorno
            elif event in ['mapa', 'rancho', 'sisbol', 'dejem']:
                self._handle_url_open(event)
        
        self.window.close()
    
    def _handle_secondary_window(self, event: str):
        """
        Gerencia a abertura de janelas secundárias.
        
        Args:
            event: Tipo de evento
        """
        self.secondary_manager.show_window(event, self.window)
    

    
    def _handle_url_open(self, event: str):
        """
        Gerencia a abertura de URLs.
        
        Args:
            event: Tipo de evento/URL
        """
        try:
            open_url(event)
        except Exception as e:
            sg.popup_error(
                f"Erro ao abrir URL: {str(e)}",
                title="Erro"
            )