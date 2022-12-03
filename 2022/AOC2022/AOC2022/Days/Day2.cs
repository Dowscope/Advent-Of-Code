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
            string[] data = AOCTools.GetData("Day2");

            foreach (string line in data)
            {
                _rounds.Add(line.Split(" "));
            }
        }

        private void _Part1()
        {
            int totalScore = 0;

            foreach (var r in _rounds)
            {
                totalScore += _PlayRound(r[0], r[1]);
            }

            AOCTools.Log("Part 1");
            AOCTools.Log("Total Score: " + totalScore);

        }

        private void _Part2()
        {
            int totalScore = 0;

            foreach (var r in _rounds)
            {
                totalScore += _PlayRoundCorrectly(r[0], r[1]);
            }

            AOCTools.Log("Part 2");
            AOCTools.Log("Total Score: " + totalScore);
        }

        // Part1 play round
        private int _PlayRound(string elf, string you)
        {
            switch (elf)
            {
                case "A":
                    switch (you)
                    {
                        case "X":
                            return 1 + 3;
                        case "Y":
                            return 2 + 6;
                        case "Z":
                            return 3 + 0;
                    }
                    break;
                case "B":
                    switch (you)
                    {
                        case "X":
                            return 1 + 0;
                        case "Y":
                            return 2 + 3;
                        case "Z":
                            return 3 + 6;
                    }
                    break;
                case "C":
                    switch (you)
                    {
                        case "X":
                            return 1 + 6;
                        case "Y":
                            return 2 + 0;
                        case "Z":
                            return 3 + 3;
                    }
                    break;
            }
            return -1;
        }

        //Part2 Play round
        private int _PlayRoundCorrectly(string elf, string you)
        {
            switch (elf)
            {
                case "A":
                    switch (you)
                    {
                        case "X":
                            return 3 + 0;
                        case "Y":
                            return 1 + 3;
                        case "Z":
                            return 2 + 6;
                    }
                    break;
                case "B":
                    switch (you)
                    {
                        case "X":
                            return 1 + 0;
                        case "Y":
                            return 2 + 3;
                        case "Z":
                            return 3 + 6;
                    }
                    break;
                case "C":
                    switch (you)
                    {
                        case "X":
                            return 2 + 0;
                        case "Y":
                            return 3 + 3;
                        case "Z":
                            return 1 + 6;
                    }
                    break;
            }
            return -1;
        }
    }
}
