#!/usr/bin/node

// Import request module
const request = require('request');

// Creation of the Url to movie API endpoint
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

// Get request to the movie API
request.get(url, async (error, response, body) => {
  if (error) console.log(error.message); // error Handler
  const film = JSON.parse(body); // Parse movie data

  // Loop through each character of the movie
  for (const character of film.characters) {
    // This promise wait for each character request end and move to the next
    await new Promise((resolve) => {
      // Get request to character API endpoint
      request.get(character, (error, response, body) => {
        if (error) console.log(error.message); // Error Handler
        const character = JSON.parse(body); // Parse character data from response body
        console.log(character.name); // Print character name
        resolve(); // Resolve the promise, end of the request
      });
    });
  }
});
