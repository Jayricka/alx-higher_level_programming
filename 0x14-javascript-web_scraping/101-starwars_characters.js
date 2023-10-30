#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    function fetchCharacter(index) {
      if (index < characterUrls.length) {
        request(characterUrls[index], (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error(`Failed to retrieve character data. Status code: ${charResponse.statusCode}`);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            fetchCharacter(index + 1);
          }
        });
      }
    }

    fetchCharacter(0);
  }
});
