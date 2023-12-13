const args = process.argv.slice(2)

let Day
switch (args[0]) {
  case '1':
    Day = require('./Days/Day1/day1')
    break
  case '2':
    Day = require('./Days/Day2/day2')
    break
  case '3':
    Day = require('./Days/Day3/day3')
    break
  case '5':
    Day = require('./Days/Day5/day5')
    break
  default:
    break
}

Day.run()