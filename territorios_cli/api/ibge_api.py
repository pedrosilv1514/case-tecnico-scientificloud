import requests
import csv
from pathlib import Path
from territorios_cli.db.sqlite_handler import inserir_territorio

DICT_PATH = Path(__file__).resolve().parent.parent / "data" / "dict.csv"

def carregar_dict():
    id_por_nome = {}
    nome_por_id = {}
    with open(DICT_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_por_nome[row["nome"].lower()] = int(row["id"])
            nome_por_id[int(row["id"])] = row["nome"]
    return id_por_nome, nome_por_id

def buscar_api_por_id(id_territorio):
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/estados/{id_territorio}/metadados"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        dimensao = data.get("area", None)

        _, nome_por_id = carregar_dict()
        nome = nome_por_id.get(int(id_territorio), "Desconhecido")

        if dimensao:
            inserir_territorio(id_territorio, nome, dimensao)
            return id_territorio, nome, dimensao
        else:
            raise ValueError("Área não encontrada em resposta da API")
    else:
        raise ConnectionError(f"Erro ao buscar território na API. Satus {response.status_code}")
    

def buscar_api_por_nome(nome_territorio):
    id_por_nome, _ = carregar_dict()
    id_territorio = id_por_nome.get(nome_territorio.lower())
    if id_territorio is None:
        raise ValueError("Nome do território não encontrado no dicionário.")
    return buscar_api_por_id(id_territorio)

