using AOC2022.Utils;

namespace AOC2022.Days
{
    internal class Day1
    {
        string currentDataFolder = Directory.GetCurrentDirectory() + "../../../../Data/";
        public Day1()
        {
            string dataPath = Path.Combine(currentDataFolder, "Day1.txt");
            string[] data = File.ReadAllLines(dataPath);
            foreach (var line in data)
            {
                AOCTools.Log(line);
            }
        }
    }
}
