using AOC2022.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2022.Days
{
    internal class Day4 : Day
    {
        private int _overlaps = 0;
        public Day4()
        {
            AOCTools.Log("AOC2022 - Day 4");
            ReadData("Day4");
            if (data.Length != 0)
            {
                Part1();
                Part2();
            }
            else
            {
                AOCTools.Log("Data file empty");
            }
        }
        public override void Part1()
        {
            _overlaps = 0;
            foreach (var line in data)
            {
                string[] elfSections = line.Split(',');
                string[] elfA = elfSections[0].Split('-');
                string[] elfB = elfSections[1].Split('-');

                
                if (Int32.Parse(elfA[0]) >= Int32.Parse(elfB[0]) && Int32.Parse(elfA[1]) <= Int32.Parse(elfB[1]))
                {
                    _overlaps++;
                }
                else if (Int32.Parse(elfB[0]) >= Int32.Parse(elfA[0]) && Int32.Parse(elfB[1]) <= Int32.Parse(elfA[1]))
                {
                    _overlaps++;
                }
            }

            AOCTools.Log("\nPart 1");
            AOCTools.Log("Total Complete Overlaps: " + _overlaps);
        }

        public override void Part2()
        {
            _overlaps = 0;

            foreach (var line in data)
            {
                string[] elfSections = line.Split(',');
                string[] elfA = elfSections[0].Split('-');
                string[] elfB = elfSections[1].Split('-');

                if (Int32.Parse(elfA[0]) >= Int32.Parse(elfB[0]) && Int32.Parse(elfA[0]) <= Int32.Parse(elfB[1]))
                {
                    _overlaps++;
                }
                else if (Int32.Parse(elfB[0]) >= Int32.Parse(elfA[0]) && Int32.Parse(elfB[0]) <= Int32.Parse(elfA[1]))
                {
                    _overlaps++;
                }
            }

            AOCTools.Log("\nPart 2");
            AOCTools.Log("Total Partial Overlaps: " + _overlaps);
        }
    }
}
