
import csv
from pathlib import Path
from datetime import datetime
from decimal import Decimal, InvalidOperation

PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = PASTA_PROJETO / "dados" / "vendas.csv"
ARQUIVO_LIMPO = PASTA_PROJETO / "dados" / "vendas_limpo.csv"
ARQUIVO_REJEITADO = PASTA_PROJETO / "dados" / "vendas_rejeitadas.csv"

COLUNAS = [
    "id_venda", "data", "produto", "categoria",
    "quantidade", "preco_unitario", "valor_total"
]


def carregar_dados():
    print("Iniciando leitura do CSV...", flush=True)

    with open(ARQUIVO_CSV, "r", encoding="utf-8-sig", newline="") as arquivo:
        amostra = arquivo.read(4096)
        arquivo.seek(0)

        try:
            separador = csv.Sniffer().sniff(
                amostra, delimiters=",;"
            ).delimiter
        except csv.Error:
            separador = ","

        leitor = csv.DictReader(arquivo, delimiter=separador)
        dados = list(leitor)

    print(f"Separador identificado: {repr(separador)}", flush=True)
    print(f"Colunas: {leitor.fieldnames}", flush=True)
    print(f"Registros encontrados: {len(dados)}", flush=True)

    return dados


def limpar_dados(dados):
    validos = []
    rejeitados = []
    ids_encontrados = set()

    for numero_linha, linha in enumerate(dados, start=2):
        try:
            id_venda = int(linha["id_venda"])
            data = datetime.strptime(
                linha["data"].strip(), "%Y-%m-%d"
            ).date()

            produto = linha["produto"].strip()
            categoria = linha["categoria"].strip()
            quantidade = int(linha["quantidade"])
            preco = Decimal(linha["preco_unitario"].strip())

            if id_venda <= 0:
                raise ValueError("ID deve ser positivo")
            if not produto or not categoria:
                raise ValueError("Produto ou categoria vazios")
            if quantidade <= 0:
                raise ValueError("Quantidade deve ser positiva")
            if not preco.is_finite() or preco < 0:
                raise ValueError("Preço inválido")
            if id_venda in ids_encontrados:
                raise ValueError("ID duplicado")

            total = (preco * quantidade).quantize(Decimal("0.01"))

            validos.append({
                "id_venda": id_venda,
                "data": data.isoformat(),
                "produto": produto,
                "categoria": categoria,
                "quantidade": quantidade,
                "preco_unitario": f"{preco:.2f}",
                "valor_total": f"{total:.2f}",
            })

            ids_encontrados.add(id_venda)

        except (ValueError, TypeError, KeyError, InvalidOperation) as erro:
            rejeitados.append({
                "linha": numero_linha,
                "motivo": str(erro),
                "dados_originais": str(linha),
            })

    return validos, rejeitados


def salvar_csv(caminho, dados, colunas):
    with open(caminho, "w", encoding="utf-8-sig", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)


def main():
    dados = carregar_dados()
    validos, rejeitados = limpar_dados(dados)

    salvar_csv(ARQUIVO_LIMPO, validos, COLUNAS)
    salvar_csv(
        ARQUIVO_REJEITADO,
        rejeitados,
        ["linha", "motivo", "dados_originais"]
    )

    total = sum(
        (Decimal(linha["valor_total"]) for linha in validos),
        Decimal("0.00")
    )

    print("\nPipeline concluído!", flush=True)
    print(f"Registros válidos: {len(validos)}", flush=True)
    print(f"Registros rejeitados: {len(rejeitados)}", flush=True)
    print(f"Faturamento: R$ {total:.2f}", flush=True)
    print("Arquivos CSV gerados.", flush=True)


if __name__ == "__main__":
    main()
