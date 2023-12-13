const fs = require('fs')

const reset = "\x1b[0m";
const red = "\x1b[31m";
const yellow = "\x1b[38;5;226m";

const data_filePath = './Days/Day5/test.txt'
// const data_filePath = './Days/Day5/testb.txt'
// const data_filePath = './Days/Day5/data.txt'

const aoc_day = "Day 5"


function partone(data){
  const lines = data.split('\r\n')
  var seeds
  var phase = -1

  for (l in lines) {
    const line = lines[l]

    if (l == 0) { seeds = lines[l].split(': ')[1].split(' ') }
    else if (lines[l] == '') { continue }
    else if (lines[l].includes(':')) { phase++ }
    else {
      const params = lines[l].split(' ')
      
    }
    console.log (`${phase}`)
  }

  return null
}

function parttwo(data){
  return null
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

function run() {
  console.log(aoc_day)
  const data = loadFile(data_filePath)

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

module.exports = {
  run: run
}