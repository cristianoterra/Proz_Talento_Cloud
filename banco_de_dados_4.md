CREATE OR REPLACE FUNCTION contando_clientes_por_dia(dia_param DATE)
RETURNS INTEGER AS $$
DECLARE
    total INTEGER;
BEGIN
    SELECT COUNT(*) INTO total
    FROM clientes
    WHERE dia_cadastro = dia_param;
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;

SELECT contando_clientes_por_dia('2023-11-19') AS total_clientes;