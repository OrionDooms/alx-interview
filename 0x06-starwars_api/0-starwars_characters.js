#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/{}/`.format(movieId);

const movieData = JSON.parse(body);

movieData.characters.forEach((characterUrl) => {
	request(characterUrl, (charError, charResponse, charBody) => {
		if (charError){
			console.log("Error:", charError);
			return;
		}
		const characterData = JSON.parse(charBody);
		console.log(characterData.name);
	});
})
;
