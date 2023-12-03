const fs = require('fs')

const test_filePath = './Days/Day1/test.txt'

function run() {
  console.log("Day 1")
  const data = loadFile(test_filePath)

  if (data == null){
    console.log('Failed reading file')
    return
  }

  const result = [
    {'Part 1': partone(data)}
  ]

  displayResults(result)
}

function partone(data){
  const lines = data.split('\n')

  

  return lines.length
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