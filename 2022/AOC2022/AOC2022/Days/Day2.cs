using AOC2022.Utils;

namespace AOC2022.Days
{
    internal class Day2
    {
        private List<string[]> _rounds = new List<string[]>();

        private Dictionary<string, int> _points = new Dictionary<string, int>()
        {
            {"A", 1},
            {"B", 2},
            {"C", 3},
            {"X", 1},
            {"Y", 2},
            {"Z", 3},
        };

        public Day2()
        {
            AOCTools.Log("AOC2022 - Day 2");
            _ReadData();
            _Part1();
            _Part2();
        }
        private void _ReadData()
        {
            string[] data = AOCTools.GetData("Day2_ex");

            foreach (string line in data)
            {
                _rounds.Add(line.Split(" "));
            }
        }

        private void _Part1()
        {

        }

        private void _Part2()
        {

        }
    }
}
