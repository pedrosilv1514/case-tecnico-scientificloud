import argparse

from territorios_cli.api.ibge_api import buscar_api_por_id, buscar_api_por_nome
from territorios_cli.db.sqlite_handler import buscar_territorio_id, buscar_territorio_nome
from territorios_cli.plot.plotter import gerar_grafico_dimensao, gerar_grafico_comparacao 

def obter_dados_territorio(valor):
    try:
        if valor.isdigit():
            dados = buscar_territorio_id(int(valor))
            if not dados:
                dados = buscar_api_por_id(int(valor))
        else:
            dados = buscar_api_por_nome(valor)
            if not dados:
                dados = buscar_api_por_nome(valor)
        return dados
    except Exception as e:
        print(f"Erro ao obter dados do território {e}")
        return None

def run_cli():
    parser = argparse.ArgumentParser(description="Análise de dimensão de territórios brasileiros")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    #Dimensão - Parser
    parser_dim = subparsers.add_parser("dimensao", help="Consulte a dimensão de um território")
    parser_dim.add_argument("--territorio", required=True, help="Nome ou ID do território")

    #Diferença - Parser
    parser_diff = subparsers.add_parser("diferenca", help="Compara dois territórios")
    parser_diff.add_argument("--t1", required=True, help="Primeiro Território (Nome ou ID)")
    parser_diff.add_argument("--t2", required=True, help="Segundo território (Nome ou ID)")

    args = parser.parse_args()

    if args.comando == "dimensao":
        dados = obter_dados_territorio(args.territorio)
        if dados:
            _, nome, dimensao = dados
            path = gerar_grafico_dimensao(nome, dimensao)
            print(f"Nome: {nome}\n Dimensão: {dimensao:.2f} km²z\n Gráfico: {path}")
        #print(f"[DEBUG] Consultar dimensão do território: {args.territorio}")

    elif args.comando == "diferenca":
        dados1 = obter_dados_territorio(args.t1)
        dados2 = obter_dados_territorio(args.t2)
        if dados1 and dados2:
            _, nome1, dim1 = dados1
            _, nome2, dim2 = dados2
            diff = abs(dim1 - dim2)
            path = gerar_grafico_comparacao(nome1, dim1, nome2, dim2)
            print(f"{nome1}: {dim1:.2f} km²\n {nome2}: {dim2:.2f} km²")
            print(f"Diferença: {diff:.2f} km² \n Gráfico: {path}")
        #print(f"[DEBUG] Comparar territórios: {args.t1} x {args.t2}")