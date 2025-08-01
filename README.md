# Sistema Auxiliar de Atendimento (APOIO 190)

<div align="center">  
    <img src="https://github.com/alexandrefreitass/auxilioatendente/assets/109884524/1795f1b7-ccf2-410e-a0db-66c295588107" alt="Tela do Sistema Auxiliar de Atendimento" width="700"/>
</div>

<br/>

<div align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
    <img src="https://img.shields.io/badge/Plataforma-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Plataforma: Windows"/>
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License: MIT"/>
</div>

## 📋 Sobre o Projeto

Este projeto é um aplicativo desktop desenvolvido em Python (utilizando a biblioteca **FreeSimpleGUI**) para auxiliar os operadores do serviço de emergência **190**. Ele oferece acesso rápido e organizado a informações cartográficas, listas de ramais e telefones úteis, visualização de rodovias e links para sistemas corporativos relevantes. O objetivo principal é **otimizar o tempo de resposta** dos atendentes, mantendo todas as informações essenciais em uma interface única e intuitiva.

## ✨ Principais Funcionalidades

- **Nota Cartográfica:** Visualização rápida de códigos de localização e referências cartográficas.  
- **Mapa CPI-2:** Acesso direto ao Google Maps configurado para a região de atuação (CPI-2).  
- **Rodovias CPI-2:** Visualizador interativo de imagens de rodovias da região (6 imagens navegáveis).  
- **Ramais:** Lista completa de ramais internos para contato rápido entre setores.  
- **Telefones:** Diretório telefônico institucional com números úteis.  
- **Sistemas Corporativos:** Atalhos diretos para sistemas internos, como Rancho, SISBOL e pesquisa de ID Dejem.

## 🚀 Primeiros Passos (Instalação)

### Pré-requisitos

- **Python 3.8+** – Certifique-se de ter o Python (versão 3.8 ou superior) instalado.  
- **Sistema Operacional:** Windows 10 ou 11 (o aplicativo foi testado nesses ambientes).  
- **Internet:** Conexão ativa para utilizar os links de sistemas corporativos (quando necessário).

### Método 1: Executável (Recomendado)

1. **Download:** Baixe o executável disponível na seção *Releases* do repositório (arquivo `auxilio-atendimento-190.exe`).  
2. **Execução:** Dê um duplo clique no executável baixado para iniciar o aplicativo imediatamente, sem necessidade de instalação.

### Método 2: Código-fonte

1. **Clonar o Repositório:** Faça o clone deste repositório em sua máquina local e navegue até o diretório do projeto:
   ```
   git clone https://github.com/alexandrefreitass/Sistema-Auxiliar-Atendimento.git
   ```
   ```
   cd Sistema-Auxiliar-Atendimento
   ```

2. **Criar Ambiente Virtual:** Dentro da pasta do projeto, crie um ambiente virtual e instale as dependências listadas:  
   ```
   python -m venv venv  
   source venv\Scripts\activate   (Bash)  
   pip install -r requirements.txt
   ```

3. **Executar a Aplicação:** Após a instalação dos pacotes, inicie o aplicativo executando o arquivo principal:  
   ```
   python src/main.py
   ```

## 📁 Estrutura do Projeto

Sistema-Auxiliar-Atendimento/  
├── src/                    # Código-fonte principal  
│   ├── main.py             # Ponto de entrada do aplicativo  
│   ├── gui/                # Interfaces gráficas (janelas e componentes de UI)  
│   ├── config/             # Configurações centralizadas do sistema  
│   └── utils/              # Funções auxiliares e utilitários  
├── assets/                 # Recursos visuais (imagens, ícones)  
├── requirements.txt        # Lista de dependências Python  
└── README.md               # Documentação do projeto

## 📦 Build do Executável

Para gerar o `.exe` a partir do código-fonte, siga estes passos:

1. Certifique-se de que o ambiente virtual está ativado:  
   ```
   source venv\Scripts\activate
   ```

2. Execute o comando abaixo na raiz do projeto:  
   ```
   pyinstaller --onefile --windowed --name=auxilio-atendimento-190 --icon=assets/icon.ico --add-data="assets;assets" src/main.py
   ```

3. O executável será gerado dentro da pasta `dist/`.

> **Dica:** Crie um atalho para `auxilio-atendimento-190.exe` para facilitar a execução pelos usuários finais.

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir com este projeto:

1. **Fork:** Realize um fork deste repositório.  
2. **Branch:** Crie uma nova branch para sua funcionalidade ou correção (`git checkout -b feature/SuaFeature`).  
3. **Commit:** Faça o commit das suas alterações (`git commit -m 'Adiciona Minha Nova Funcionalidade'`).  
4. **Push:** Envie a branch para o seu repositório remoto (`git push origin feature/SuaFeature`).  
5. **Pull Request:** Abra um Pull Request neste repositório original e aguarde a revisão das suas alterações.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
