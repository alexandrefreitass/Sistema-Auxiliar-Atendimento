"""
Gerenciador de janelas secundárias - Design Moderno
"""

import FreeSimpleGUI as sg
from typing import Callable, Optional

from ..config.settings import (
    FONT_PADRAO, EVENT_IMAGES, COLORS, FONTS, 
    BUTTON_CONFIGS, BUTTON_ICONS, RODOVIA_IMAGES
)
from ..utils.helpers import get_asset_path


class SecondaryWindowManager:
    """Gerencia as janelas secundárias do aplicativo com design moderno."""
    
    def __init__(self, return_callback: Callable):
        """
        Inicializa o gerenciador de janelas secundárias.
        
        Args:
            return_callback: Função a ser chamada quando voltar à tela principal
        """
        self.return_callback = return_callback
        self.current_image_index = 0
        self.total_images = len(RODOVIA_IMAGES)
        self._setup_theme()
    
    def _setup_theme(self):
        """Configura o tema das janelas secundárias."""
        sg.theme('Dark')
    
    def show_window(self, event: str, main_window: sg.Window):
        """
        Exibe uma janela secundária moderna baseada no evento.
        
        Args:
            event: Tipo de evento (nota, telefones, ramais)
            main_window: Janela principal a ser fechada
        """
        layout = self._get_layout(event)
        main_window.close()
        
        # Títulos personalizados para cada janela
        titles = {
            'nota': f"{BUTTON_ICONS['nota']} Nota Cartográfica",
            'telefones': f"{BUTTON_ICONS['telefones']} Diretório de Telefones",
            'ramais': f"{BUTTON_ICONS['ramais']} Lista de Ramais Internos",
            'rodovia': f"{BUTTON_ICONS['rodovia']} Rodovias CPI-2"
        }
        
        title = titles.get(event, event.capitalize())
        
        secondary_window = sg.Window(
            title,
            layout,
            font=FONT_PADRAO,
            finalize=True,
            element_justification='c',
            margins=(20, 20),
            resizable=False,
            modal=False
        )
        
        self._handle_secondary_window(secondary_window)
    
    def _get_layout(self, event: str) -> list:
        """
        Retorna o layout moderno para a janela secundária.
        
        Args:
            event: Tipo de evento
            
        Returns:
            Layout da janela com design atualizado
        """
        if event in EVENT_IMAGES or event == 'rodovia':
            # Para rodovias, usar a primeira imagem inicialmente
            if event == 'rodovia':
                image_path = get_asset_path(RODOVIA_IMAGES[self.current_image_index])
            else:
                image_path = get_asset_path(EVENT_IMAGES[event])
            
            # Descrições para cada tipo de conteúdo
            descriptions = {
                'nota': 'Consulte as informações cartográficas e códigos de referência',
                'telefones': 'Diretório completo de telefones institucionais e emergenciais',
                'ramais': 'Lista de ramais internos organizados por setor e função',
                'rodovia': f'Visualizando rodovia {self.current_image_index + 1} de {self.total_images} - Use os botões para navegar'
            }
            
            description = descriptions.get(event, 'Informações do sistema')
            
            return [
                # Cabeçalho
                [sg.Text(f'{BUTTON_ICONS.get(event, "📄")} {event.upper()}',
                        font=FONTS['subtitle'],
                        pad=((0, 0), (15, 5)))],
                
                [sg.Text(description,
                        font=FONTS['caption'],
                        justification='center',
                        pad=((0, 0), (5, 15)))],
                
                [sg.HorizontalSeparator(pad=((50, 50), (10, 15)))],
                
                # Imagem principal
                [sg.Image(filename=image_path, 
                         key='-IMAGE-',
                         pad=((10, 10), (10, 10)))],
                
                # Controles específicos para rodovias
                [sg.HorizontalSeparator(pad=((50, 50), (15, 15)))],
                
                # Controles de navegação (apenas para rodovias)
                self._get_navigation_controls(event),
                
                [sg.Button('⬅️ Voltar ao Menu', 
                          key="Voltar", 
                          size=(12, 2),
                          button_color=('white', COLORS['surface']),
                          font=FONTS['caption'],
                          pad=((0, 0), (10, 15)))],
                
                # Rodapé
                [sg.Text('Pressione ESC ou clique em Voltar para retornar',
                        font=FONTS['caption'],
                        justification='center',
                        pad=((0, 0), (10, 15)))]
            ]
        else:
            return [
                [sg.Text('❌ Evento não suportado',
                        font=FONTS['subtitle'],
                        justification='center',
                        pad=((0, 0), (20, 20)))],
                
                [sg.Text('O conteúdo solicitado não foi encontrado ou não está disponível.',
                        font=FONTS['body'],
                        justification='center',
                        pad=((0, 0), (10, 20)))],
                
                [sg.Button('⬅️ Voltar ao Menu', 
                          key="Voltar", 
                          size=(12, 2),
                          button_color=('white', COLORS['surface']),
                          font=FONTS['caption'])]
            ]
    
    def _get_navigation_controls(self, event: str) -> list:
        """
        Retorna controles de navegação específicos para cada tipo de evento.
        
        Args:
            event: Tipo de evento
            
        Returns:
            Lista com controles de navegação
        """
        if event == 'rodovia':
            return [
                sg.Button('⬅️ Anterior', key='-PREV-', 
                         size=(10, 1), 
                         button_color=('white', COLORS['primary_blue']), 
                         font=FONTS['caption']),
                sg.Text(f'{self.current_image_index + 1}/{self.total_images}',
                       key='-INFO-',
                       font=FONTS['caption'],
                       justification='center',
                       size=(8, 1)),
                sg.Button('➡️ Próximo', key='-NEXT-', 
                         size=(10, 1), 
                         button_color=('white', COLORS['primary_blue']), 
                         font=FONTS['caption'])
            ]
        else:
            return []
    
    def _handle_secondary_window(self, window: sg.Window):
        """
        Gerencia os eventos da janela secundária.
        
        Args:
            window: Janela secundária
        """
        while True:
            event, values = window.read()
            
            if event in (sg.WINDOW_CLOSED, 'Voltar'):
                window.close()
                self.return_callback()
                break
            elif event == 'Escape:27':  # Tecla ESC
                window.close()
                self.return_callback()
                break
            elif event == '-NEXT-':
                self._next_image(window)
            elif event == '-PREV-':
                self._prev_image(window)
    
    def _next_image(self, window: sg.Window):
        """Vai para a próxima imagem de rodovia."""
        self.current_image_index = (self.current_image_index + 1) % self.total_images
        self._update_rodovia_image(window)
    
    def _prev_image(self, window: sg.Window):
        """Vai para a imagem anterior de rodovia."""
        self.current_image_index = (self.current_image_index - 1) % self.total_images
        self._update_rodovia_image(window)
    
    def _update_rodovia_image(self, window: sg.Window):
        """Atualiza a imagem de rodovia exibida."""
        try:
            # Carregar nova imagem
            image_path = get_asset_path(RODOVIA_IMAGES[self.current_image_index])
            window['-IMAGE-'].update(filename=image_path)
            
            # Atualizar contador
            window['-INFO-'].update(f'{self.current_image_index + 1}/{self.total_images}')
            
        except Exception as e:
            sg.popup_error(
                f"❌ Erro ao carregar imagem:\n{str(e)}",
                title="Erro"
            )