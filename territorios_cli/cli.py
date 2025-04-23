#print("[DEBUG] Iniciando execução do CLI")
try:
    import argparse
    #print("[DEBUG] Importado argparse")
    from territorios_cli.api.ibge_api import buscar_api_por_id, buscar_api_por_nome
    #print("[DEBUG] Importado ibge_api")
    from territorios_cli.db.sqlite_handler import buscar_territorio_id, buscar_territorio_nome
    #print("[DEBUG] Importado sqlite_handler")
    from territorios_cli.plot.plotter import gerar_grafico_dimensao, gerar_grafico_comparacao
    #print("[DEBUG] Importado plotter")
    from pathlib import Path
except ImportError as e:
    print(f"[ERRO] Falha ao importar módulos: {e}")
    import sys
    sys.exit(1)


def obter_dados_territorio(valor):
    try:
        #print(f"[DEBUG] Buscando dados para: {valor}")
        dados = None

        if valor.isdigit():
            dados = buscar_territorio_id(int(valor))
            #print(f"[DEBUG] Dados no banco: {dados}")
            if not dados:
                dados = buscar_api_por_id(int(valor))
                #print(f"[DEBUG] Dados da API: {dados}")
        else:
            dados = buscar_territorio_nome(valor)
            #print(f"[DEBUG] Dados no banco: {dados}")
            if not dados:
                dados = buscar_api_por_nome(valor)
                #print(f"[DEBUG] Dados da API: {dados}")
        return dados
    except Exception as e:
        #print(f"[DEBUG] Erro ao obter dados do território: {e}")
        return None


def definir_caminho(nome, tipo, output_arg):
    try:
        path = Path(output_arg)
        if path.parent.exists():
            return path
    except Exception:
        pass
    pasta_default = Path(__file__).resolve().parent / "outputs"
    pasta_default.mkdir(exist_ok=True)
    return pasta_default / f"{nome} - {tipo}.png"


def run_cli():
    #print("[DEBUG] Iniciando execução do CLI")
    parser = argparse.ArgumentParser(description="Análise de dimensão de territórios brasileiros")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # Dimensão - Parser
    parser_dim = subparsers.add_parser("dimensao", help="Consulte a dimensão de um território")
    parser_dim.add_argument("--territorio", required=True, help="Nome ou ID do território")
    parser_dim.add_argument("--output", required=False, help="Caminho para salvar a imagem gerada")

    # Diferença - Parser
    parser_diff = subparsers.add_parser("diferenca", help="Compara dois territórios")
    parser_diff.add_argument("--t1", required=True, help="Primeiro Território (Nome ou ID)")
    parser_diff.add_argument("--t2", required=True, help="Segundo território (Nome ou ID)")
    parser_diff.add_argument("--output", required=False, help="Caminho para salvar a imagem gerada")

    args = parser.parse_args()

    if args.comando == "dimensao":
        #print(f"[DEBUG] Consultando dimensão para: {args.territorio}")
        dados = obter_dados_territorio(args.territorio)
        if dados:
            _, nome, dimensao = dados
           #print(f"[DEBUG] Dados encontrados - Nome: {nome}, Dimensão: {dimensao}")
            path = definir_caminho(nome, "Dimensao", args.output)
            gerar_grafico_dimensao(nome, dimensao, path)
            print(f"Nome: {nome}\nDimensão: {dimensao:.2f} km²\nGráfico: {path}")
        else:
            print("[DEBUG] Nenhum dado encontrado para o território.")

    elif args.comando == "diferenca":
        #print(f"[DEBUG] Comparando territórios: {args.t1} e {args.t2}")
        dados1 = obter_dados_territorio(args.t1)
        dados2 = obter_dados_territorio(args.t2)
        if dados1 and dados2:
            _, nome1, dim1 = dados1
            _, nome2, dim2 = dados2
            diff = abs(dim1 - dim2)
            nome_combinado = f"{nome1} vs {nome2}"
            path = definir_caminho(nome_combinado, "Comparacao", args.output)
            gerar_grafico_comparacao(nome1, dim1, nome2, dim2, path)
            print(f"{nome1}: {dim1:.2f} km²\n{nome2}: {dim2:.2f} km²")
            print(f"Diferença: {diff:.2f} km²\nGráfico: {path}")
        else:
            print("[DEBUG] Não foi possível comparar os territórios.")


if __name__ == "__main__":
    run_cli()
