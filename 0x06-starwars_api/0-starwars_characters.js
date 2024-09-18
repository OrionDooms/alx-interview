#!/usr/bin/node
/* Importing the request module allowing to make HTTP requests to the api */
const result = require('request');
/* Get the ID from command line arguments */
const Id = process.argv[2];
const Url = 'https://swapi-api.alx-tools.com/api/films/' + Id;

result(Url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  /* The result accepts three arguments: error, response, body */
  const movie = JSON.parse(body);
  movie.characters.forEach((characterUrl) => {
    result(characterUrl, (charError, charResponse, charBody) => {
      const Data = JSON.parse(charBody);
      console.log(Data.name);
    });
  });
});
