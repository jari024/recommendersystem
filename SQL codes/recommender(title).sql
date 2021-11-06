/* Creating the database for the Starring recommendation*/
CREATE DATABASE recommendertitle;

/* Creating the tables for the recommendation system */
CREATE TABLE moviestitle (
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
\copy moviestitle FROM '/home/pi/RSL/moviesFromMetacritic.csv' delimiter ';' CSV header;
SELECT * FROM moviestitle WHERE url='pirates-of-the-caribbean-the-curse-of-the-black-pearl';

/* Adding a table for the tsVector for Starring */
ALTER TABLE moviestitle ADD lexemesTitle tsvector;

/* Updating the lexemes for starring to make it into tsvector */
UPDATE moviestitle SET lexemesTitle = to_tsvector(Title);

/* Testing there are enough results with Depp in it */
SELECT url FROM moviestitle WHERE lexemesTitle @@ to_tsquery('pirates');

/* Adding a table with a closeness rating as a float to determine how close a movie is */
ALTER TABLE moviestitle ADD rank float4;
UPDATE moviestitle SET rank = ts_rank(lexemesTitle,plainto_tsquery(( SELECT Title FROM movies WHERE url='pirates-of-the-caribbean-the-curse-of-the-black-pearl')));
CREATE TABLE recommendationsBasedOnTitleField AS SELECT url, rank FROM movies WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/top50recommendations-title.csv' WITH csv;
