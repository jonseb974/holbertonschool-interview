#!/usr/bin/node

const fetch = require('node-fetch');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

async function getCharacters () {
  try {
    const response = await fetch(url);
    const film = await response.json();
    for (const characterUrl of film.characters) {
      const characterResponse = await fetch(characterUrl);
      const character = await characterResponse.json();
      console.log(character.name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

getCharacters();
