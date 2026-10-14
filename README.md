# Pipeline de Engenharia de Dados — Vendas
# Sales Data Engineering Pipeline

## 🇧🇷 Português

### Sobre o projeto

Este projeto implementa um pipeline de dados de vendas utilizando Python e SQLite. O objetivo é demonstrar um fluxo de Engenharia de Dados que envolve leitura, validação, transformação, armazenamento e análise de dados.

O pipeline processa um arquivo CSV, separa os registros válidos dos rejeitados, calcula o valor total de cada venda e carrega os dados tratados em um banco de dados SQLite.

### Objetivos

- Automatizar o processamento de dados de vendas.
- Validar e transformar dados de origem.
- Separar registros válidos e rejeitados.
- Calcular o valor total das vendas.
- Armazenar os dados em um banco de dados relacional.
- Criar consultas SQL para análise de negócios.

### Tecnologias utilizadas

- **Python:** processamento, validação e transformação dos dados.
- **CSV:** formato dos dados de entrada e saída.
- **SQLite:** armazenamento dos dados tratados.
- **SQL:** consultas e análises de vendas.
- **DB Browser for SQLite:** visualização e execução de consultas no banco.
- **Visual Studio Code:** ambiente de desenvolvimento.

### Estrutura do projeto

```text
engenharia-dados-pipeline/
├── dados/
│   ├── vendas.csv
│   ├── vendas_limpo.csv
│   └── vendas_rejeitadas.csv
├── src/
│   ├── pipeline.py
│   └── carregar_banco.py
├── banco/
│   └── vendas.db
├── sql/
│   └── consultas.sql
└── README.md
```

### Etapas do pipeline

1. **Extração:** leitura dos dados do arquivo `vendas.csv`.
2. **Validação:** verificação dos dados para identificar registros inválidos.
3. **Transformação:** cálculo do valor total de cada venda, multiplicando a quantidade pelo preço unitário.
4. **Separação:** geração dos arquivos de dados limpos e rejeitados.
5. **Carga:** armazenamento dos registros válidos na tabela `vendas`, no SQLite.
6. **Análise:** execução de consultas SQL para gerar indicadores de vendas.

### Resultados do processamento

| Indicador | Resultado |
|---|---:|
| Registros processados | 10 |
| Registros válidos | 10 |
| Registros rejeitados | 0 |
| Itens vendidos | 24 |
| Faturamento total | R$ 18.780,00 |
| Ticket médio por venda | R$ 1.878,00 |

Os resultados correspondem à base de dados de exemplo utilizada neste projeto.

### Análises SQL

O arquivo `sql/consultas.sql` contém consultas para:

- Visualizar os registros de vendas.
- Contar os registros armazenados.
- Calcular o faturamento total e o ticket médio.
- Analisar o faturamento por produto.
- Comparar o desempenho das categorias.
- Acompanhar o faturamento por data.
- Criar um ranking de produtos por faturamento.

### Como executar

**Requisitos:** Python 3 instalado e um sistema operacional com suporte a SQLite.

1. Abra a pasta do projeto no Visual Studio Code.
2. Execute `src/pipeline.py` para processar o CSV.
3. Execute `src/carregar_banco.py` para carregar os dados no banco SQLite.
4. Abra `banco/vendas.db` no DB Browser for SQLite.
5. Acesse a aba **Execute SQL** para executar as consultas disponíveis em `sql/consultas.sql`.

O projeto utiliza bibliotecas da biblioteca padrão do Python, incluindo `csv`, `sqlite3` e `decimal`, sem necessidade de instalar bibliotecas externas.

### Aprendizados

Este projeto demonstra conhecimentos iniciais de Engenharia de Dados, incluindo processamento de arquivos, validação de dados, tratamento de valores monetários, persistência em banco de dados e análise com SQL.

---

## 🇺🇸 English

### About the project

This project implements a sales data pipeline using Python and SQLite. Its purpose is to demonstrate a data engineering workflow involving data ingestion, validation, transformation, storage, and analysis.

The pipeline processes a CSV file, separates valid and rejected records, calculates the total value of each sale, and loads the cleaned data into a SQLite database.

### Project objectives

- Automate sales data processing.
- Validate and transform source data.
- Separate valid and rejected records.
- Calculate total sales values.
- Store processed data in a relational database.
- Create SQL queries for business analysis.

### Technologies

- **Python:** data processing, validation, and transformation.
- **CSV:** input and output data format.
- **SQLite:** processed data storage.
- **SQL:** sales queries and analysis.
- **DB Browser for SQLite:** database inspection and query execution.
- **Visual Studio Code:** development environment.

### Project structure

```text
engenharia-dados-pipeline/
├── dados/
│   ├── vendas.csv
│   ├── vendas_limpo.csv
│   └── vendas_rejeitadas.csv
├── src/
│   ├── pipeline.py
│   └── carregar_banco.py
├── banco/
│   └── vendas.db
├── sql/
│   └── consultas.sql
└── README.md
```

### Pipeline stages

1. **Extraction:** reads data from `vendas.csv`.
2. **Validation:** checks the source data for invalid records.
3. **Transformation:** calculates each sale's total by multiplying quantity by unit price.
4. **Separation:** generates cleaned and rejected data files.
5. **Loading:** stores valid records in the SQLite `vendas` table.
6. **Analysis:** executes SQL queries to produce sales indicators.

### Processing results

| Metric | Result |
|---|---:|
| Records processed | 10 |
| Valid records | 10 |
| Rejected records | 0 |
| Items sold | 24 |
| Total revenue | BRL 18,780.00 |
| Average sale value | BRL 1,878.00 |

These results correspond to the sample dataset used in this project.

### SQL analysis

The `sql/consultas.sql` file includes queries to:

- Inspect sales records.
- Count stored records.
- Calculate total revenue and average sale value.
- Analyze revenue by product.
- Compare category performance.
- Track revenue by date.
- Rank products by revenue.

### How to run

**Requirements:** Python 3 and a system with SQLite support.

1. Open the project folder in Visual Studio Code.
2. Run `src/pipeline.py` to process the CSV file.
3. Run `src/carregar_banco.py` to load the data into SQLite.
4. Open `banco/vendas.db` using DB Browser for SQLite.
5. Use the **Execute SQL** tab to run the queries in `sql/consultas.sql`.

The project uses Python standard-library modules, including `csv`, `sqlite3`, and `decimal`, with no external package installation required.

### Key learnings

This project demonstrates foundational data engineering skills, including file processing, data validation, monetary value handling, database persistence, and SQL-based analysis.

---

## Author

Data Engineering Portfolio Project