## Aplicativo de Auxílio ao Atendimento 190

<div align="center">
    <img src="https://github.com/alexandrefreitass/auxilioatendente/assets/109884524/1795f1b7-ccf2-410e-a0db-66c295588107" />
</div>

### Visão Geral
Este aplicativo desktop foi desenvolvido utilizando Python e FreeSimpleGUI para auxiliar operadores do serviço de emergência 190. Oferece acesso rápido e organizado a informações cartográficas, ramais, telefones, visualizador de rodovias e links para sistemas corporativos. O objetivo é otimizar o tempo de resposta dos atendentes, mantendo todas as informações essenciais em uma interface única e intuitiva.

### Funcionalidades
- **Nota Cartográfica**: Visualização rápida de códigos e referências
- **Mapa CPI-2**: Acesso direto ao Google Maps configurado para a região
- **Rodovias CPI-2**: Visualizador interativo de imagens de rodovias (6 imagens navegáveis)
- **Ramais**: Lista completa de ramais internos
- **Telefones**: Diretório telefônico institucional  
- **Sistemas Corporativos**: Links diretos para Rancho, SISBOL e Pesquisa ID Dejem

### Estrutura do Projeto
```
pipsimplegui/
├── src/                    # Código-fonte principal
│   ├── main.py            # Ponto de entrada
│   ├── gui/               # Interfaces gráficas
│   ├── config/            # Configurações centralizadas
│   └── utils/             # Funções auxiliares
├── assets/                # Recursos visuais (imagens, ícones)
├── requirements.txt       # Dependências Python
└── README.md             # Esta documentação
```

### Pré-requisitos
Para executar este aplicativo, você precisa ter instalado em seu sistema:
- Python 3.8 ou superior
- Windows (testado no Windows 10/11)
- Conexão com internet para sistemas corporativos

### Instalação e Execução

#### Método 1: Executável (Recomendado)
1. Baixe o executável da seção Releases
2. Execute diretamente: `auxilio-atendimento-190.exe`

#### Método 2: Código-fonte
1. Clone o repositório:
   ```bash
   git clone https://github.com/alexandrefreitass/auxilioatendente.git
   cd pipsimplegui
   ```

2. Crie um ambiente virtual e instale dependências:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   python src/main.py
   ```

### Desenvolvimento

#### Construir Executável
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name=auxilio-atendimento-190 --icon=assets/icon.ico --add-data=assets;assets src/main.py
```

#### Estrutura Modular
- **`src/gui/main_window.py`**: Interface principal com todos os botões
- **`src/gui/image_viewer.py`**: Visualizador de rodovias com navegação
- **`src/gui/secondary_windows.py`**: Janelas para ramais/telefones/nota cartográfica
- **`src/config/settings.py`**: Configurações centralizadas (URLs, caminhos, visual)
- **`src/utils/helpers.py`**: Funções auxiliares (carregamento de imagens, validações)

### Configuração
As configurações estão centralizadas em `src/config/settings.py` incluindo:
- URLs dos sistemas corporativos
- Caminhos de imagens e recursos
- Configurações visuais e tema
- Mapeamento de eventos para imagens

### Licença
Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---
**Desenvolvido por Alexandre Freitas para os operadores do 190**