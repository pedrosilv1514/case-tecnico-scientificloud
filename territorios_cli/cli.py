import argparse

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
        print(f"[DEBUG] Consultar dimensão do território: {args.territorio}")
    
    elif args.comando == "diferenca":
        print(f"[DEBUG] Comparar territórios: {args.t1} x {args.t2}")