--Em 4.sql, escreva uma consulta SQL que liste os nomes de todas as músicas que tenham dançabilidade, energia e valência maiores que 0,75.
SELECT name FROM songs where danceability > 0.75 and energy > 0.75 and valence > 0.75;