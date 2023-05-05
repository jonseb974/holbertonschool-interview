#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach(function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  });
});
