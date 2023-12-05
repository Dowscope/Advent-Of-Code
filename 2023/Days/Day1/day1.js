const fs = require('fs')

const reset = "\x1b[0m";
const red = "\x1b[31m";
const yellow = "\x1b[38;5;226m";

// const test_filePath = './Days/Day1/test.txt'
const test_filePath = './Days/Day1/testb.txt'
// const test_filePath = './Days/Day1/data.txt'

function run() {
  console.log("Day 1")
  const data = loadFile(test_filePath)

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
  const lines = data.split('\n')

  var result = 0

  for (var l of lines) {
    const numbers = l.match(/\d/g)

    // console.log(`Line OG: ${l}`)
    if (numbers != null){
      const strNum = parseInt(numbers[0] + numbers[numbers.length-1])
      // console.log(`Line number: ${strNum}`)
      result += strNum
    }
    else {
      console.log(red + `This line has no numbers: ${l}` + reset)
    }
  }

  return result
}

function parttwo(data){
  console.log(yellow + "Part Two" + reset)
  var newData = cleanString(data)
  newData = cleanString(newData)

  return partone(newData)
}

function cleanString(data) {
  const newData = data.replace(/(one|two|three|four|five|six|seven|eight|nine)/gi, (m) => {
    const wordToNumberMap = {
      zero: 'z0o',
      one: 'o1e',
      two: 't2o',
      three: 't3e',
      four: 'f4r',
      five: 'f5e',
      six: 's6x',
      seven: 's7n',
      eight: 'e8t',
      nine: 'n9e'
    };
    const replacement = wordToNumberMap[m.toLowerCase()];
    // console.log(`OG: ${m} Replacement: ${replacement}`)
    return replacement !== undefined ? replacement : m;
  })
  return newData
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