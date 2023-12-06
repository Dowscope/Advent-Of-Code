const fs = require("fs");

const reset = "\x1b[0m";
const red = "\x1b[31m";
const yellow = "\x1b[38;5;226m";

const input_filePath = "./Days/Day3/test.txt";
// const input_filePath = './Days/Day3/data.txt'

function run() {
  console.log("Day 3");
  const data = loadFile(input_filePath);

  if (data == null) {
    console.log("Failed reading file");
    return;
  }

  const result = [
    { "Part 1": partone(data) },
    // {'Part 2': parttwo(data)}
  ];

  displayResults(result);
}

function isDigit(character) {
  const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
  return numbers.includes(character);
}

function isSymbol(character) {
  const symbolRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?]+/;
  return symbolRegex.test(character);
}

function partone(data) {
  console.log(yellow + "Part One" + reset);
  var result = 0;

  const lines = data.split('\n')

  const part_numbers = []

  for (const i in lines){
    const l = parseInt(i)
    const characters = lines[l].split('')
    const num = {
      n: '',
      startingIndex: -1
    }

    for (const c in characters){
      if (c == characters.length - 1){
        if (num.startingIndex != -1) {
          const starting_y = l - 1 < 0 ? l : l - 1
          const ending_y = l + 1 >= lines.length ? l : l + 1
          
          for (y = starting_y; y < ending_y; y++) {
            const starting_x = num.startingIndex - 1 < 0 ? num.startingIndex : num.startingIndex - 1
            const ending_x = starting_x + num.n.length >= characters.length ? starting_x + num.n.length - 1 : starting_x + num.n.length
            console.log(`SX: ${starting_x} | SY: ${starting_y} | ${ending_x} | ${ending_y}`)
            for (x = starting_x; x < ending_x; x++) {
              console.log(y,x)
            }
          }
          
          num.n = ''
          num.startingIndex = -1
          continue
        }
      }

      if (isDigit(characters[c])){
        if (num.startingIndex == -1){
          num.n = characters[c]
          num.startingIndex =  c
        }
        else {
          num.n += characters[c]
        }
      }
      else {
        if (num.startingIndex != -1){
          const starting_y = l - 1 < 0 ? l : l - 1
          const ending_y = l + 1 >= lines.length ? l : l + 1
          for (y = starting_y; y < ending_y; y++) {
            const starting_x = num.startingIndex - 1 < 0 ? num.startingIndex : num.startingIndex - 1
            const ending_x = starting_x + num.n.length >= characters.length ? starting_x + num.n.length - 1 : starting_x + num.n.length
            console.log(`SX: ${starting_x} | SY: ${starting_y} | ${ending_x} | ${ending_y}`)
            for (x = starting_x; x < ending_x; x++) {
              console.log(y,x)
            }
          }

          num.n = ''
          num.startingIndex = -1
        }
      }
    }
  }

  result = lines.length


  return result;
}

function parttwo(data) {
  console.log(yellow + "Part Two" + reset);
  const lines = data.split("\r\n");

  var result = 0;

  for (var l of lines) {
  }

  return result;
}

function displayResults(data) {
  console.log("The Results");
  console.log("-----------");
  console.log(data);
}

function loadFile(path) {
  process.stdout.write(`Reading File: ${path}... `);
  try {
    const data = fs.readFileSync(path, "utf8");
    console.log("Successful");
    return data;
  } catch (error) {
    console.log(`Failed\nError reading file ${path}. \n${error}`);
    return null;
  }
}

module.exports = {
  run: run,
};
