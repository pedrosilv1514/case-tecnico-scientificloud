<h1 align="center">
  Case Técnico - Scientificloud
</h1>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img alt="Sqlite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white">

</div>

<div align="center">
    <img alt="Tamanho do código do projeto" src="https://img.shields.io/github/languages/code-size/pedrosilv1514/case-tecnico-scientificloud" />
</div>

## Sobre o repositório

Este é um projeto de linha de comando (CLI) para consulta e comparação de dimensões de territórios brasileiros, com dados provenientes da API do IBGE e um banco de dados local SQLite para armazenamento em cache.

## Funcionalidades

- Consultar a dimensão (em km²) de um território brasileiro.

- Comparar a dimensão entre dois territórios.

- Gerar gráficos de barra salvos como imagens .png.

- Buscar os dados prioritariamente no banco local e, se não encontrados, recorrer à API do IBGE.

## Estrutura do Projeto
```
territorios_cli/
├── api/
│   └── ibge_api.py
├── db/
│   └── sqlite_handler.py
├── plot/
│   └── plotter.py
├── data/
│   └── dict.csv
├── cli.py
├── outputs/ (gerado automaticamente)
```
## Requisitos

- Bibliotecas:
  - requests
  - matplotlib

## Configuração

Como forma de melhor organização e versacionamento das dependências do código. É obrigatório instalar as bibliotecas necessárias para sua execução. Antes, necessita a configuração de um ambiente virtual:

```bash

#Criar o ambiente virutal
python -m venv venv

#Ativar o ambiente virtual (Linux)
source venv/bin/activate

# Windows
./venv/Scripts/activate

#Instalar requisitos necessários
pip install -r requirements.txt
```
## Execução

O script principal é o ```cli.py```, localizado na raiz do pacote territorios_cli.

### 1. Consultar a dimensão de um território

```bash
python -m territorios_cli.cli dimensao --territorio "Acre"
```
Caso não forneça um caminho especifíco para o gráfico, uma pasta outputs será criada e armazenará os gráficos obtidos.

### 2. Comparar dois territórios

```bash
python -m territorios_cli.cli diferenca --t1 "Acre" --t2 "Amazonas"
```

### 3. Salvar o gráfico em um caminho específico (ex: Downloads)

```bash
python -m territorios_cli.cli dimensao --territorio "Acre" --output "C:/Users/user_nanme/Downloads"
```

## Observações

- Caso o caminho do --output seja inválido ou não fornecido, o arquivo será salvo na pasta outputs/.

- A API do IBGE pode retornar dados no formato inesperado para alguns estados. Isso é tratado no código e mensagens de debug são exibidas.

<h2>💻 Autor</h2>

<table>
  <tr>
    <td align="center"><a href="https://github.com/pedrosilv1514" target="_blank"><img style="border-radius: 50%;" src="https://github.com/pedrosilv1514.png" width="100px;" alt="Pedro Henrique"/><br /><sub><b>Pedro Henrique</b></sub></a><br/
</table>


