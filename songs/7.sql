-- Em 7.sql, escreva uma consulta SQL que retorne a energia média das músicas de Drake
select avg(songs.energy)
from songs
join artists on songs.artist_id = artists.id
where artists.name = 'Drake';