#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL of the Star Wars API.');
  process.exit(1);
}

const characterId = 18; // ID for Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    const numberOfMoviesWithWedgeAntilles = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    ).length;

    console.log(numberOfMoviesWithWedgeAntilles);
  }
});
