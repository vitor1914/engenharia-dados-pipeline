
import csv
import sqlite3
from pathlib import Path

# Caminhos do projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = PASTA_PROJETO / "dados" / "vendas_limpo.csv"
PASTA_BANCO = PASTA_PROJETO / "banco"
ARQUIVO_BANCO = PASTA_BANCO / "vendas.db"


def criar_tabela(conexao):
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id_venda INTEGER PRIMARY KEY,
            data TEXT NOT NULL,
            produto TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL CHECK (quantidade > 0),
            preco_unitario NUMERIC NOT NULL CHECK (preco_unitario >= 0),
            valor_total NUMERIC NOT NULL CHECK (valor_total >= 0)
        )
    """)
    conexao.commit()
    print("Tabela vendas criada ou já existente.", flush=True)


def carregar_dados(conexao):
    if not ARQUIVO_CSV.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {ARQUIVO_CSV}\n"
            "Execute primeiro o arquivo pipeline.py."
        )

    with open(ARQUIVO_CSV, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = list(leitor)

    registros = []

    for linha in dados:
        registros.append((
            int(linha["id_venda"]),
            linha["data"],
            linha["produto"],
            linha["categoria"],
            int(linha["quantidade"]),
            float(linha["preco_unitario"]),
            float(linha["valor_total"]),
        ))

    conexao.executemany("""
        INSERT INTO vendas (
            id_venda, data, produto, categoria,
            quantidade, preco_unitario, valor_total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id_venda) DO UPDATE SET
            data = excluded.data,
            produto = excluded.produto,
            categoria = excluded.categoria,
            quantidade = excluded.quantidade,
            preco_unitario = excluded.preco_unitario,
            valor_total = excluded.valor_total
    """, registros)

    conexao.commit()
    print(f"Registros processados: {len(registros)}", flush=True)


def consultar_resumo(conexao):
    resultado = conexao.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(quantidade), 0),
            COALESCE(SUM(valor_total), 0)
        FROM vendas
    """).fetchone()

    total_vendas = resultado[0] or 0
    itens_vendidos = resultado[1] or 0
    faturamento = float(resultado[2] or 0)

    print("\nResumo do banco:", flush=True)
    print(f"Vendas cadastradas: {total_vendas}", flush=True)
    print(f"Itens vendidos: {itens_vendidos}", flush=True)
    print(f"Faturamento: R$ {faturamento:.2f}", flush=True)


def main():
    print("Iniciando carregamento do banco...", flush=True)

    PASTA_BANCO.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(ARQUIVO_BANCO) as conexao:
        criar_tabela(conexao)
        carregar_dados(conexao)
        consultar_resumo(conexao)

    print(f"\nBanco salvo em: {ARQUIVO_BANCO}", flush=True)
    print("Execução finalizada.", flush=True)


if __name__ == "__main__":
    main()
