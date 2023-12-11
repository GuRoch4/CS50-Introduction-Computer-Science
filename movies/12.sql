select movies.title from movies
join stars as star_jo on movies.id = star_jo.movie_id
join people as jo on star_jo.person_id = jo.id
join stars as star_he on movies.id = star_he.movie_id
join people as he on star_he.person_id = he.id
WHERE jo.name = 'Johnny Depp' AND he.name = 'Helena Bonham Carter';