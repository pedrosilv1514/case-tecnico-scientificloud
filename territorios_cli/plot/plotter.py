import matplotlib.pyplot as plt
from pathlib import Path

def gerar_grafico_dimensao(nome, dimensao, output_path=None):
    plt.figure(figsize=(6, 6))
    barras = plt.bar([nome], [dimensao], color='skyblue')
    plt.title(f"Dimensão de {nome}")
    plt.ylabel("Área (km²)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.text(0, dimensao, f"{dimensao:,.0f}", ha='center', va='bottom', fontsize=10)
    plt.tight_layout()

    nome_arquivo = f"{nome} - Dimensão.png"
    caminho_final = _resolver_output_path(output_path, nome_arquivo)
    plt.savefig(caminho_final)
    plt.close()
    return caminho_final


def gerar_grafico_comparacao(nome1, dim1, nome2, dim2, output_path=None):
    plt.figure(figsize=(8, 6))
    nomes = [nome1, nome2]
    dimensoes = [dim1, dim2]
    nomes_dimensoes = sorted(zip(nomes, dimensoes), key=lambda x: x[1], reverse=True)
    nomes, dimensoes = zip(*nomes_dimensoes)

    barras = plt.bar(nomes, dimensoes, color=['green', 'orange'])
    plt.title("Comparação de Dimensões")
    plt.ylabel("Área (km²)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for barra, valor in zip(barras, dimensoes):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height(), f"{valor:,.0f}",
                 ha='center', va='bottom', fontsize=9)

    plt.tight_layout()

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
