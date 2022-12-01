using AOC2022.Utils;

namespace AOC2022.Days
{
    internal class Day1
    {
        string currentDataFolder = Directory.GetCurrentDirectory() + "../../../../Data/";
        string dataPath;
        string[] data;

        // This is the list of elves and what they are holding.
        Dictionary<int, int> elvesCalories = new Dictionary<int, int>();
        Dictionary<int, int> topThreeCalories = new Dictionary<int, int>();

        public Day1()
        {
            AOCTools.Log("AOC2022 - Day 1");

            _ReadData();
            _Part1();
            _Part2();
        }

        private void _ReadData()
        {
            dataPath = Path.Combine(currentDataFolder, "Day1.txt");
            data = File.ReadAllLines(dataPath);

            int elfIndex = 1;
            int totalCalories = 0;

            foreach (var line in data)
            {
                if (line.Length == 0)
                {
                    elvesCalories.Add(elfIndex, totalCalories);
                    elfIndex++;
                    totalCalories = 0;
                    continue;
                }

                totalCalories += Int32.Parse(line);
            }

            // Add the last bit to the dictionary.
            elvesCalories.Add(elfIndex, totalCalories);
        }

        private void _Part1()
        {
            // Find the top elf
            var results = elvesCalories.OrderByDescending(x => x.Value).ToArray();
            AOCTools.Log("\nPart 1");
            AOCTools.Log("Top Elf is " + results[0].Key + " with total calories of " + results[0].Value);
        }

        private void _Part2()
        {
            var results = elvesCalories.OrderByDescending(x => x.Value).Take(3).ToArray();
            int totalCalories = 0;
            foreach (var r in results)
            {
                totalCalories += r.Value;
            }

            AOCTools.Log("\nPart 2");
            AOCTools.Log("Top Three Total Calories: " + totalCalories);
        }
    }
}
