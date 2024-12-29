--Let's take a look at the data

select *
from `movieSet.Movie_data`


/*
Some released year and country are different than the actual year and country in the table.
Let's create 2 new column with year_correct and country_correct
*/

ALTER TABLE movieSet.Movie_data
ADD column year_correct int64

update movieSet.Movie_data
set year_correct = substring(released, strpos (released, ",")+1, 5 )

ALTER TABLE movieSet.Movie_data
ADD column country_correct string

update movieSet.Movie_data
set country_correct =  SUBSTR(released, STRPOS(released, '(') + 1, STRPOS(released, ')') - STRPOS(released, '(') - 1)


select *
from `movieSet.Movie_data`
where name is null

--create a new temporary table to remove null data

with new_movie_data as (
  select *
  from `movieSet.Movie_data`
  where COALESCE(name, rating, genre, year, released,score,votes, director, writer, star,country, budget, gross, company, runtime) is not null
   
)
select *
from new_movie_data
order by gross



with new_movie_data as (
  select *
  from `movieSet.Movie_data`
  where name is not null and
   rating is not null and 
   genre is not null and 
   year is not null and 
   released is not null and 
   score is not null and 
   votes is not null and 
   director is not null and  
   writer is not null and 
   star is not null and 
   country is not null and  
   budget is not null and 
   gross is not null and  
   company is not null and  
   runtime is not null
   
)
select company, gross, budget, runtime, score, released
from new_movie_data
order by gross desc

create view movieSet.new_movie_data as 
   select *
   from `movieSet.Movie_data`
   where name is not null and
     rating is not null and 
     genre is not null and 
     year is not null and 
     released is not null and 
     score is not null and 
     votes is not null and 
     director is not null and  
     writer is not null and 
     star is not null and 
     country is not null and  
     budget is not null and 
     gross is not null and  
     company is not null and  
     runtime is not null  

--let's see if the null values where removed

select *
from `movieSet.new_movie_data`
where gross is null

select *
from `movieSet.new_movie_data`
where runtime is null

/*
We have created a new table with no null value and with new release year and country since some released year and country are different then the original table year and country
*/



