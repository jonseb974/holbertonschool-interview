#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a GET request to the Star Wars API to get the movie details
request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);

  let characterCount = 0;
  movie.characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error.message}`);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      characterCount++;
      console.log(`${characterCount}. ${character.name}`);

      if (characterCount === movie.characters.length) {
        // All characters have been retrieved, exit the program
        process.exit(0);
      }
    });
  });
});
