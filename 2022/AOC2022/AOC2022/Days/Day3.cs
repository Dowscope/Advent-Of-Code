using AOC2022.Utils;
using System.Diagnostics.Metrics;
using System;

namespace AOC2022.Days
{
    internal class Day3 : Day
    {
        private List<string[]> _rucksackCompartments= new List<string[]>();
        private string _alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"; 

        public Day3(string day): base(day)
        {
            AOCTools.Log("AOC2022 - Day 3");
            ReadData("Day3");
            if (data.Length != 0)
            {
                _ReadRucksack();
                Part1();
                Part2();
            }
            else
            {
                AOCTools.Log("Data file empty");
            }
            
        }

        private void _ReadRucksack()
        {
            foreach (var line in data)
            {
                string first = line.Substring(0, line.Length/2);
                string second = line.Substring(line.Length/2);

                string[] compartments = { first, second, line };
                _rucksackCompartments.Add(compartments);
            }
        }

        public override void Part1()
        {
            int prioritySum = 0;

            foreach (var c in _rucksackCompartments)
            {
                string found = "";

                foreach (var letter in c[0])
                {
                    if (c[1].Contains(letter) && !found.Contains(letter))
                    {
                        int index = _alphabet.IndexOf(letter) + 1;
                        prioritySum += index;
                        found += letter;
                    }
                }
            }

            AOCTools.Log("\nPart 1");
            AOCTools.Log("The priority sum is: " + prioritySum);
        }

        public override void Part2()
        {
            int prioritySum = 0;

            for (int i = 0; i < _rucksackCompartments.Count - 2; i = i + 3)
            {
                string found = "";

                foreach (var letter in _rucksackCompartments[i][2])
                {
                    if (_rucksackCompartments[i + 1][2].Contains(letter) &&
                        _rucksackCompartments[i + 2][2].Contains(letter) &&
                        !found.Contains(letter))
                    {
                        int index = _alphabet.IndexOf(letter) + 1;
                        prioritySum += index;
                        found += letter;
                    }
                }
            }

            AOCTools.Log("\nPart 2");
            AOCTools.Log("The priority sum is: " + prioritySum);
        }
    }
}
