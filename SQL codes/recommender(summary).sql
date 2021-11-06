/* Creating the database for the Starring recommendation*/
CREATE DATABASE recommender(summary);

/* Creating the tables for the recommendation system */
CREATE TABLE movies (
url text,
title text,
releaseDate text,
Distributor text,
Starring text,
Summary text,
Director text,
Genre text,
Rating text,
Runtime text,
Userscore text,
Metascore text,
scoreCounts text
);

/* Importing the dataset and checking the data*/
\copy movies FROM '/home/pi/RSL/moviesFromMetacritic.csv' delimiter ';' CSV header;
SELECT * FROM movies WHERE url='pirates-of-the-caribbean-the-curse-of-the-black-pearl';

/* Adding a table for the tsVector for Starring */
ALTER TABLE movies ADD lexemesSummary tsvector;

/* Updating the lexemes for starring to make it into tsvector */
UPDATE movies SET lexemesSummary = to_tsvector(Summary);

/* Testing there are enough results with Depp in it */
SELECT url FROM movies WHERE lexemesSummary @@ to_tsquery('pirate');

/* Adding a table with a closeness rating as a float to determine how close a movie is */
ALTER TABLE movies ADD rank float4;
UPDATE movies SET rank = ts_rank(lexemesSummary,plainto_tsquery(( SELECT Summary FROM movies WHERE url='pirates-of-the-caribbean-the-curse-of-the-black-pearl')));
CREATE TABLE recommendationsBasedOnSummaryField AS SELECT url, rank FROM movies WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnSummaryField) to '/home/pi/RSL/top50recommendations-title.csv' WITH csv;
