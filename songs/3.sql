--Em 3.sql, escreva uma consulta SQL para listar os nomes das 5 músicas mais longas, em ordem decrescente de duração.
SELECT name FROM songs order by duration_ms desc limit 5;