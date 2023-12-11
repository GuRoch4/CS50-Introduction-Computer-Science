-- Em 8.sql, escreva uma consulta SQL que liste os nomes das músicas que apresentam outros artistas
select name from songs
where name like '%feat%'