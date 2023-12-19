CREATE OR REPLACE FUNCTION levantamento_diario()
RETURNS TABLE (data_venda DATE, total_de_vendas INT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        data_venda,
        SUM(quantidade) AS total_de_vendas
    FROM vendas
    GROUP BY data_venda
    ORDER BY data_venda;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM levantamento_diario();