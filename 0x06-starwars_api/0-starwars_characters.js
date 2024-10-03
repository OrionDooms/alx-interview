#!/usr/bin/node
/* Importing the request module allowing to make HTTP requests to the api */
const request = require('request');
const id = process.argv[2];
/* The Url points to the Star wars API */
const Url = 'https://swapi-api.alx-tools.com/api/films/' + id;

if (!id || !Url) {
  process.exit(1);
}
/* This function fetch the movie data */
request(Url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
    return;
  }
  const movieData = JSON.parse(body).characters;
  /* fetch each character's */
  const StarWarCharacter = movieData.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
          return;
        }
        const Data = JSON.parse(charBody);
        resolve(Data.name);
      });
    });
  });
  /* all character names are fetch and printed in order */
  Promise.all(StarWarCharacter)
    .then((Names) => {
      Names.forEach((name) => console.log(name));
    })
    .catch((err) => console.error(err));
});
