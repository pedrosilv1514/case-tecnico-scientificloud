import matplotlib.pyplot as plt
from pathlib import Path
import uuid

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def gerar_grafico_dimensao(nome, dimensao, output_path=None):
    print(f"[DEBUG] Gerando gráfico para {nome} com dimensão {dimensao}")
    plt.figure(figsize=(6,4))
    plt.bar([nome], [dimensao], color="skyblue")
    plt.ylabel("Dimensão (km²)")
    plt.title(f"Dimensão do território: {nome}")
    plt.tight_layout()

    filename = f"dimensao_{uuid.uuid4().hex[:8]}.png"
    filepath = Path(output_path) if output_path else OUTPUT_DIR / filename
    plt.savefig(filepath)
    plt.close()

    print(f"[DEBUG] Gráfico gerado: {filepath}")
    return filepath

def gerar_grafico_comparacao(nome1, dimensao1, nome2, dimensao2, output_path=None):
    print(f"[DEBUG] Gerando gráfico de comparação entre {nome1} e {nome2}")
    plt.figure(figsize=(8,5))
    plt.bar([nome1, nome2], [dimensao1, dimensao2], color=['skyblue', 'orange'])
    plt.ylabel("Dimensão (km²)")
    plt.title(f"Comparação entre {nome1} e {nome2}")

    plt.tight_layout()
    filename = f"diferenca_{uuid.uuid4().hex[:8]}.png"
    filepath = Path(output_path) if output_path else OUTPUT_DIR / filename
    plt.savefig(filepath)
    plt.close()

    print(f"[DEBUG] Gráfico de comparação gerado: {filepath}")
    return filepath
