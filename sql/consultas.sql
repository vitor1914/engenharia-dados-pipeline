
-- 1. Consultar todas as vendas
SELECT *
FROM vendas
ORDER BY data;

-- 2. Faturamento total
SELECT
    SUM(valor_total) AS faturamento_total
FROM vendas;

-- 3. Faturamento por produto
SELECT
    produto,
    SUM(quantidade) AS quantidade_vendida,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC;

-- 4. Faturamento por categoria
SELECT
    categoria,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY categoria
ORDER BY faturamento DESC;

-- 5. Resumo geral
SELECT
    COUNT(*) AS total_vendas,
    SUM(quantidade) AS itens_vendidos,
    ROUND(AVG(valor_total), 2) AS ticket_medio,
    SUM(valor_total) AS faturamento_total
FROM vendas;
