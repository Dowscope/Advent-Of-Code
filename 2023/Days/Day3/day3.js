const fs = require('fs')

const reset = "\x1b[0m";
const red = "\x1b[31m";
const yellow = "\x1b[38;5;226m";

const input_filePath = './Days/Day3/test.txt'
// const input_filePath = './Days/Day3/data.txt'

function run() {
  console.log("Day 3")
  const data = loadFile(input_filePath)

  if (data == null){
    console.log('Failed reading file')
    return
  }

  const result = [
    {'Part 1': partone(data)},
    // {'Part 2': parttwo(data)}
  ]

  displayResults(result)
}

function isDigit(character) {
  const numbers = ['0', '1','2','3','4','5','6','7','8','9']
  console.log(character, numbers.includes(character))
  return numbers.includes(character)
}

function isSymbol(character) {
  const symbolRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?]+/
  return symbolRegex.test(character)
}

function partone(data){
  console.log(yellow + "Part One" + reset)
  const lines = data.split('\r\n')

  var result = 0

  for (var l in lines) {
    var cols = lines[l].split('')

    var num = {
      n: '',
      startIndex: -1,
    }

    for (var c in cols) {
      console.log(c)
      if (isDigit(cols[c])) {
        num.n += cols[c]
        if (num.startIndex == -1){
          num.startIndex = c
        }
      }
      else {
        if (num.startIndex != -1) {
          const length_of_num = num.n.length

          var y = l - 1 < 0 ? l : l - 1
          var x = num.startIndex - 1 < 0 ? num.startIndex : num.startIndex - 1

          const x_boundary = parseInt(num.startIndex) + parseInt(length_of_num)

          const y_end = l + 1 >= lines.length ? l : l + 1
          const x_end = x_boundary + 1 >= cols.length ? x_boundary : x_boundary + 1

          console.log(`Stats: ${num.startIndex} | ${length_of_num} | ${lines.length - 1} | ${cols.length - 1}`)
          console.log(`l: ${l}`)
          console.log(`y: ${y} | x: ${x}`)
          console.log(`y_end: ${y_end} | x_endL ${x_end}`)

          for (y; y <= y_end; y++) {
            for (x; x <= x_end; x++) {
              console.log(`Symbol ${lines[l][c]} | Located at ${x}, ${y}`)
            }
            x = num.startIndex - 1 < 0 ? num.startIndex : num.startIndex - 1
          }

          num = {
            n: '',
            startIndex: -1,
          }
        }
      }
    }
  }

  return result
}

function parttwo(data){
  console.log(yellow + "Part Two" + reset)
  const lines = data.split('\r\n')

  var result = 0

  for (var l of lines) {
    
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