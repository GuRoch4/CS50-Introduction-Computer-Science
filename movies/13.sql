select people.name from people
join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
join stars as star_kevin on star_kevin.movie_id = movies.id
join people as people_kevin on people_kevin.id = star_kevin.person_id
where people_kevin.name = "Kevin Bacon" and people_kevin.birth = 1958 and people.name != "Kevin Bacon";