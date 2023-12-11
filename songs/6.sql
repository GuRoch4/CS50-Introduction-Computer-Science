-- Em 6.sql, escreva uma consulta SQL que liste os nomes das músicas de Post Malone
select songs.name
from songs
join artists on songs.artist_id = artists.id
where artists.name = 'Post Malone';