#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;
  const characterNames = [];

  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      characterNames.push(character.name);

      if (characterNames.length === characterUrls.length) {
        characterNames.forEach((name) => console.log(name));
      }
    });
  });
});
