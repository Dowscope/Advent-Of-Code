const fs = require('fs')

const reset = "\x1b[0m";
const red = "\x1b[31m";
const yellow = "\x1b[38;5;226m";

// const input_filePath = './Days/Day2/test.txt'
const input_filePath = './Days/Day2/data.txt'

function run() {
  console.log("Day 2")
  const data = loadFile(input_filePath)

  if (data == null){
    console.log('Failed reading file')
    return
  }

  const result = [
    {'Part 1': partone(data)},
    {'Part 2': parttwo(data)}
  ]

  displayResults(result)
}

function partone(data){
  console.log(yellow + "Part One" + reset)
  const lines = data.split('\r\n')

  var result = 0

  const bag = {
    'red': 12,
    'green': 13,
    'blue': 14
  }

  for (var l of lines) {
    const game = l.split(':')[0].split(' ')[1]
    const cubes_played = l.split(':')[1].split(';')

    var game_possible = true
    for (const cubes of cubes_played) {
      const cube_sets = cubes.split(', ')

      for (const set of cube_sets) {
        const s = set.trim().split(' ')
        if (s[0] > bag[s[1]]) {
          game_possible = false
        }
      }
    }

    if (game_possible) {
      result += parseInt(game)
    }
  }

  return result
}

function parttwo(data){
  console.log(yellow + "Part Two" + reset)
  const lines = data.split('\r\n')

  var result = 0

  for (var l of lines) {
    const game = l.split(':')[0].split(' ')[1]
    const cubes_played = l.split(':')[1].split(';')

    const bag = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    for (const cubes of cubes_played) {
      const cube_sets = cubes.split(', ')

      for (const set of cube_sets) {
        const s = set.trim().split(' ')
        if (s[0] > bag[s[1]]) {
          bag[s[1]] = parseInt(s[0])
        }
      }
    }

    result += bag['red'] * bag['green'] * bag['blue']
  }

  return result
}


function displayResults(data){
  console.log("The Results")
  console.log("-----------")
  console.log(data)
}

function loadFile(path) {
  process.stdout.write(`Reading File: ${path}... `)
  try {
    const data = fs.readFileSync(path, 'utf8')
    console.log("Successful")
    return data
  } catch (error) {
    console.log(`Failed\nError reading file ${path}. \n${error}`)
    return null
  }
}

module.exports = {
  run: run
}