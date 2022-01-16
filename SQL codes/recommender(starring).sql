/* Creating the database for the Starring recommendation*/
CREATE DATABASE recommenderstarring;

/* Creating the tables for the recommendation system */
CREATE TABLE moviesstarring (
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
\copy moviesstarring FROM '/home/pi/RSL/moviesFromMetacritic.csv' delimiter ';' CSV header;
SELECT * FROM moviesstarring WHERE url='harry-potter-and-the-sorcerers-stone';

/* Adding a table for the tsVector for Starring */
ALTER TABLE moviesstarring ADD lexemesStarring tsvector;

/* Updating the lexemes for starring to make it into tsvector */
UPDATE moviesstarring SET lexemesStarring = to_tsvector(Starring);

/* Testing there are enough results with Depp in it */
SELECT url FROM moviesstarring WHERE lexemesStarring @@ to_tsquery('Radcliffe');

/* Adding a table with a closeness rating as a float to determine how close a movie is */
ALTER TABLE moviesstarring ADD rank float4;
UPDATE moviesstarring SET rank = ts_rank(lexemesStarring,plainto_tsquery(( SELECT Summary FROM moviesstarring WHERE url='harry-potter-and-the-sorcerers-stone')));
CREATE TABLE recommendationsBasedOnStarringField AS SELECT url, rank FROM moviesstarring WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnStarringField) to '/home/pi/RSL/top50recommendations-starring.csv' WITH csv;
