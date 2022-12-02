namespace AOC2022.Utils
{
    internal class AOCTools
    {
        public static string[] GetData(string day)
        {
            string dataPath = Directory.GetCurrentDirectory() + "../../../../Data/" + day + ".txt";
            return File.ReadAllLines(dataPath);
        }
        public static void Log(string message)
        {
            Console.WriteLine(message);
        }

        public static void Log(char message)
        {
            Console.WriteLine(message);
        }

        public static void Log(int message)
        {
            Console.WriteLine(message);
        }
    }
}
