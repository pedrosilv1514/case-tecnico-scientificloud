import requests
import csv
import sqlite3
from pathlib import Path
from territorios_cli.db.sqlite_handler import inserir_territorio, buscar_territorio_id

DICT_PATH = Path(__file__).resolve().parent.parent / "data" / "dict.csv"

def carregar_dict():
    id_por_nome = {}
    nome_por_id = {}
    try:
        with open(DICT_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id_por_nome[row["nome"].lower()] = int(row["id"])
                nome_por_id[int(row["id"])] = row["nome"]
        return id_por_nome, nome_por_id
    except Exception as e:
        print(f"[ERRO] Falha ao carregar dicionário: {e}")
        return {}, {}

def extrair_dimensao(data):
    if isinstance(data, (int, float)):
        return float(data)
    elif isinstance(data, dict):
        for key in ['area', 'dimensao', 'valor', 'area_km2']:
            if key in data:
                valor = data[key]
                if isinstance(valor, (int, float)) or (isinstance(valor, str) and valor.replace('.', '', 1).isdigit()):
                    return float(valor)
        for value in data.values():
            if isinstance(value, (int, float)):
                return float(value)
    return None

def buscar_api_por_id(id_territorio):
    dados_existentes = buscar_territorio_id(id_territorio)
    if dados_existentes:
        return dados_existentes

    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/estados/{id_territorio}/metadados"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Falha ao acessar API (status {response.status_code})")
        
        data = response.json()
        if not data:
            raise ValueError("Dados vazios da API")
        if isinstance(data, list):
            data = data[0]

        dimensao = extrair_dimensao(data.get("area"))
        if dimensao is None:
            raise ValueError("Área não encontrada na resposta")

        _, nome_por_id = carregar_dict()
        nome = nome_por_id.get(int(id_territorio), f"Estado {id_territorio}")

        try:
            inserir_territorio(id_territorio, nome, dimensao)
        except sqlite3.IntegrityError:
            return buscar_territorio_id(id_territorio)

        return id_territorio, nome, dimensao

    except Exception as e:
        raise ValueError(f"Erro ao buscar dados na API: {e}")

def buscar_api_por_nome(nome_territorio):
    id_por_nome, _ = carregar_dict()
    id_territorio = id_por_nome.get(nome_territorio.lower())

    if not id_territorio:
        raise ValueError(f"Nome não encontrado no CSV: {nome_territorio}")
    
    return buscar_api_por_id(id_territorio)
