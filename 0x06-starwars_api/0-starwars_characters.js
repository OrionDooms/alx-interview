#!/usr/bin/node
/* Importing the request module allowing to make HTTP requests to the api */
const request = require('request');
/* Get the ID from command line arguments */
const Id = process.argv[2];
const Url = 'https://swapi-api.alx-tools.com/api/films/' + Id;

if (!Id || !Url) {
  process.exit(1);
}

request(Url, (error, response, body) => {
  if (response.statusCode === 200 || !error) {
  /* The result accepts three arguments: error, response, body */
    const film = JSON.parse(body);

    if (film.characters.length !== 0) {
      film.characters.forEach((characterUrl) => {
        request(characterUrl, (acterError, acterResponse, acterBody) => {
          const Starwars = JSON.parse(acterBody);
          console.log(Starwars.name);
        });
      });
    }
  }
});
