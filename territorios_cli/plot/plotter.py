import matplotlib.pyplot as plt
from pathlib import Path

def gerar_grafico_dimensao(nome, dimensao, output_path=None):
    plt.figure(figsize=(6, 6))
    plt.bar([nome], [dimensao], color='skyblue')
    plt.title(f"Dimensão de {nome}")
    plt.ylabel("Área (km²)")

    nome_arquivo = f"{nome} - Dimensão.png"
    caminho_final = _resolver_output_path(output_path, nome_arquivo)
    plt.savefig(caminho_final)
    plt.close()
    return caminho_final

def gerar_grafico_comparacao(nome1, dim1, nome2, dim2, output_path=None):
    plt.figure(figsize=(8, 6))
    plt.bar([nome1, nome2], [dim1, dim2], color=['green', 'orange'])
    plt.title("Comparação de Dimensões")
    plt.ylabel("Área (km²)")

    nome_arquivo = f"{nome1} vs {nome2} - Comparação.png"
    caminho_final = _resolver_output_path(output_path, nome_arquivo)
    plt.savefig(caminho_final)
    plt.close()
    return caminho_final

def _resolver_output_path(output_path, nome_arquivo):
    try:
        if output_path:
            caminho = Path(output_path)
            if caminho.is_dir():
                return caminho / nome_arquivo
            elif caminho.suffix == '':
                Path("outputs").mkdir(exist_ok=True)
                return Path("outputs") / nome_arquivo
            else:
                return caminho
    except Exception:
        pass
    Path("outputs").mkdir(exist_ok=True)
    return Path("outputs") / nome_arquivo
