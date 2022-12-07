using AOC2022.Utils;

namespace AOC2022.Days
{
    internal class Day6 : Day
    {
        public Day6(string day) : base(day)
        {
            AOCTools.Log("AOC2022 - Day 6");
            ReadData("Day6");
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
            for (int i = 4; i < data[0].Length; i++)
            {
                if (data[0].Substring(i-4, 4).Distinct().Count() == 4)
                {
                    AOCTools.Log("\nPart 1\nThe marker is: " + i);
                    break;
                }
            }
        }

        public override void Part2()
        {
            for (int i = 14; i < data[0].Length; i++)
            {
                if (data[0].Substring(i - 14, 14).Distinct().Count() == 14)
                {
                    AOCTools.Log("\nPart 2\nThe marker is: " + i);
                    break;
                }
            }
        }
    }
}
