const args = process.argv.slice(2)

let Day
switch (args[0]) {
  case '1':
    Day = require('./Days/Day1/day1')
    break
  case '2':
    Day = require('./Days/Day2/day2')
    break
  default:
    break
}

Day.run()