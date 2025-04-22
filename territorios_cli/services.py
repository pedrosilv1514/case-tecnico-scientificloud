from territorios_cli.db.sqlite_handler import buscar_territorio_id, buscar_territorio_nome
from territorios_cli.api.ibge_api import buscar_api_por_id, buscar_api_por_nome
from territorios_cli.plot.plotter import gerar_grafico_dimensao, gerar_grafico_comparacao
from territorios_cli.api.ibge_api import carregar_dict


def buscar_dados(entrada):
    id_por_nome, nome_por_id = carregar_dict()

    try:
        id_territorio = int(entrada)
        registro = buscar_territorio_id(id_territorio)
        if registro:
            return registro[1], registro[2]
        else:
            _, nome, dimensao = buscar_api_por_id(id_territorio)
            return nome, dimensao
    except ValueError:
        nome = entrada.lower()
        registro = buscar_territorio_nome(nome)
        if registro:
            return registro[1], registro[2]
        else:
            _, nome, dimensao = buscar_api_por_nome(nome)
            return nome, dimensao


def processar_dimensao(entrada):
    nome, dimensao = buscar_dados(entrada)
    caminho_img = gerar_grafico_dimensao(nome, dimensao)

    print(f"\n📍 Território: {nome}")
    print(f"📏 Dimensão: {dimensao:.2f} km²")
    print(f"📊 Gráfico salvo em: {caminho_img}")


def processar_diferenca(entrada1, entrada2):
    nome1, dim1 = buscar_dados(entrada1)
    nome2, dim2 = buscar_dados(entrada2)

    caminho_img = gerar_grafico_comparacao(nome1, dim1, nome2, dim2)
    diff = abs(dim1 - dim2)

    print(f"\n📍 {nome1}: {dim1:.2f} km²")
    print(f"📍 {nome2}: {dim2:.2f} km²")
    print(f"📐 Diferença: {diff:.2f} km²")
    print(f"📊 Gráfico salvo em: {caminho_img}")
