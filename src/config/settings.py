"""
Configurações centralizadas do aplicativo - Design Moderno
"""

import os

# ========== DESIGN SYSTEM ==========

# Paleta de Cores Moderna (Tema Polícia/Emergência)
COLORS = {
    # Cores Primárias
    'primary_blue': '#1e3a8a',      # Azul polícia moderno
    'primary_red': '#dc2626',       # Vermelho emergência
    'accent_blue': '#3b82f6',       # Azul claro
    'accent_red': '#ef4444',        # Vermelho claro
    
    # Cores Secundárias
    'dark_bg': '#0f172a',           # Fundo escuro
    'medium_bg': '#1e293b',         # Fundo médio
    'light_bg': '#334155',          # Fundo claro
    'surface': '#475569',           # Superfície
    
    # Texto
    'text_primary': '#f8fafc',      # Texto principal
    'text_secondary': '#cbd5e1',    # Texto secundário
    'text_accent': '#60a5fa',       # Texto destaque
    
    # Status
    'success': '#10b981',           # Verde sucesso
    'warning': '#f59e0b',           # Amarelo alerta
    'error': '#ef4444',             # Vermelho erro
    
    # Gradientes
    'gradient_primary': ['#1e3a8a', '#3b82f6'],
    'gradient_accent': ['#dc2626', '#ef4444']
}

# Tipografia Moderna
FONTS = {
    'title': ('Segoe UI', 24, 'bold'),
    'subtitle': ('Segoe UI', 16, 'bold'),
    'body': ('Segoe UI', 11, 'normal'),
    'button': ('Segoe UI', 12, 'bold'),
    'caption': ('Segoe UI', 9, 'normal')
}

# ========== CONFIGURAÇÕES DE INTERFACE ==========

# Configurações Gerais
FONT_PADRAO = FONTS['body']
TEMA_PADRAO = "Dark"  # Tema customizado será aplicado

# Configurações de Botões Modernas
BUTTON_CONFIGS = {
    'primary': {
        'size': (18, 3),
        'pad': ((10, 10), (8, 8)),
        'button_color': ('white', COLORS['primary_blue']),
        'font': FONTS['button']
    },
    'secondary': {
        'size': (18, 3),
        'pad': ((10, 10), (8, 8)),
        'button_color': ('white', COLORS['primary_red']),
        'font': FONTS['button']
    },
    'navigation': {
        'size': (12, 2),
        'pad': ((5, 5), (5, 5)),
        'button_color': ('white', COLORS['surface']),
        'font': FONTS['caption']
    }
}

# Configuração do Título Principal
TITLE_CONFIG = {
    'font': FONTS['title'],
    'pad': ((0, 0), (20, 30)),
    'justification': 'center'
}

# Configuração de Texto Secundário
SUBTITLE_CONFIG = {
    'font': FONTS['subtitle'],
    'pad': ((0, 0), (0, 20)),
    'justification': 'center'
}

# ========== CONFIGURAÇÕES DE JANELAS ==========

# Janela Principal
MAIN_WINDOW_SIZE = (600, 700)
MAIN_WINDOW_TITLE = "🚨 APOIO 190 - Sistema de Suporte Operacional"
MAIN_WINDOW_CONFIG = {
    'margins': (20, 20)
}

# Visualizador de Imagens
IMAGE_VIEWER_SIZE = (550, 650)
IMAGE_VIEWER_TITLE = "🛣️ Visualizador de Rodovias CPI-2"
IMAGE_DISPLAY_SIZE = (520, 580)
IMAGE_VIEWER_CONFIG = {
    'margins': (15, 15)
}

# ========== ÍCONES E SÍMBOLOS ==========

# Ícones para os botões (usando Unicode)
BUTTON_ICONS = {
    'nota': '📋',
    'mapa': '🗺️',
    'rodovia': '🛣️',
    'rancho': '🍽️',
    'ramais': '📞',
    'sisbol': '📊',
    'telefones': '☎️',
    'dejem': '🔍'
}

# Textos dos botões com ícones
BUTTON_TEXTS = {
    'nota': f"{BUTTON_ICONS['nota']} Nota Cartográfica",
    'mapa': f"{BUTTON_ICONS['mapa']} Mapa CPI-2",
    'rodovia': f"{BUTTON_ICONS['rodovia']} Rodovias CPI-2",
    'rancho': f"{BUTTON_ICONS['rancho']} Sistema Rancho",
    'ramais': f"{BUTTON_ICONS['ramais']} Ramais Internos",
    'sisbol': f"{BUTTON_ICONS['sisbol']} SISBOL",
    'telefones': f"{BUTTON_ICONS['telefones']} Telefones",
    'dejem': f"{BUTTON_ICONS['dejem']} Pesquisar ID Dejem"
}

# ========== RECURSOS EXISTENTES ==========

# Caminhos de Assets
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets')

# Imagens de Rodovias
RODOVIA_IMAGES = [
    "rodovia-1.png", "rodovia-2.png", "rodovia-3.png",
    "rodovia-4.png", "rodovia-5.png", "rodovia-6.png"
]

# Mapeamento de Imagens para Eventos
EVENT_IMAGES = {
    'nota': "cong.png",
    'telefones': "telefones.png",
    'ramais': "ramais.png"
}

# URLs dos Sistemas Corporativos
URLS = {
    'mapa': "https://www.google.com/maps/d/u/0/viewer?hl=pt-BR&mid=16KbTEVrLWKzLdamU_juPp-XvpbBiTSgF&ll=-23.021202234164612%2C-46.7070392565535&z=10",
    'rancho': "http://weblinux.intranet.policiamilitar.sp.gov.br/35bpmi/rancho/",
    'sisbol': "http://sisbol.intranet.policiamilitar.sp.gov.br/_sisbolsc8/frmlogin/",
    'dejem': "http://www.copom.intranet.policiamilitar.sp.gov.br/tecnologia/controle_dejem_por_id/"
}

# ========== CONFIGURAÇÕES LEGACY (Compatibilidade) ==========

# Mantido para compatibilidade com código existente
BUTTON_CONFIG = BUTTON_CONFIGS['primary']
TEXT_CONFIG = TITLE_CONFIG