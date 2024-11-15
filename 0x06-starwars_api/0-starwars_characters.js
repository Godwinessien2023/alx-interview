#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <n>');
  process.exit(1);
}

const id = process.argv[2];
if (isNaN(id)) {
  console.log('<n> must be an integer');
  process.exit(1);
}

function promiseRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

async function printChars () {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  try {
    const response = await promiseRequest(url);
    const characters = response.characters;
    for (const character of characters) {
      const body = await promiseRequest(character);
      const name = body.name;
      console.log(name);
    }
  } catch (err) {
    console.error(err);
  }
}

printChars();
