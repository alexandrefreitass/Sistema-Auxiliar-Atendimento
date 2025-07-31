"""
Funções auxiliares para o aplicativo.
"""

import os
import webbrowser
from typing import List
from PIL import Image, ImageTk

from ..config.settings import ASSETS_DIR, URLS


def get_asset_path(filename: str) -> str:
    """
    Retorna o caminho completo para um arquivo de asset.
    
    Args:
        filename: Nome do arquivo na pasta assets
        
    Returns:
        Caminho completo para o arquivo
    """
    return os.path.join(ASSETS_DIR, filename)


def load_image(filename: str, size: tuple = None) -> ImageTk.PhotoImage:
    """
    Carrega uma imagem do diretório de assets.
    
    Args:
        filename: Nome do arquivo de imagem
        size: Tupla (largura, altura) para redimensionar a imagem
        
    Returns:
        Objeto ImageTk.PhotoImage
    """
    image_path = get_asset_path(filename)
    image = Image.open(image_path)
    
    if size:
        image = image.resize(size)
    
    return ImageTk.PhotoImage(image)


def load_images(filenames: List[str], size: tuple = None) -> List[ImageTk.PhotoImage]:
    """
    Carrega múltiplas imagens do diretório de assets.
    
    Args:
        filenames: Lista com nomes dos arquivos de imagem
        size: Tupla (largura, altura) para redimensionar as imagens
        
    Returns:
        Lista de objetos ImageTk.PhotoImage
    """
    return [load_image(filename, size) for filename in filenames]


def open_url(url_key: str) -> None:
    """
    Abre uma URL no navegador padrão.
    
    Args:
        url_key: Chave da URL no dicionário de configurações
    """
    if url_key in URLS:
        webbrowser.open(URLS[url_key])
    else:
        print(f"URL não encontrada para a chave: {url_key}")


def validate_assets() -> bool:
    """
    Valida se todos os arquivos de assets necessários existem.
    
    Returns:
        True se todos os assets existem, False caso contrário
    """
    from ..config.settings import RODOVIA_IMAGES, EVENT_IMAGES
    
    # Verificar diretório de assets
    if not os.path.exists(ASSETS_DIR):
        print(f"Diretório de assets não encontrado: {ASSETS_DIR}")
        return False
    
    # Verificar imagens de rodovias
    for img in RODOVIA_IMAGES:
        if not os.path.exists(get_asset_path(img)):
            print(f"Imagem de rodovia não encontrada: {img}")
            return False
    
    # Verificar imagens de eventos
    for img in EVENT_IMAGES.values():
        if not os.path.exists(get_asset_path(img)):
            print(f"Imagem de evento não encontrada: {img}")
            return False
    
    return True