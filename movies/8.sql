select people.name from people
join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
where movies.title like "Toy Story%";