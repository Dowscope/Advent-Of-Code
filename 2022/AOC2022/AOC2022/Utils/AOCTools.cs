namespace AOC2022.Utils
{
    internal class AOCTools
    {
        public static string[] GetData(string day)
        {
            string dataPath = Directory.GetCurrentDirectory() + "../../../../Data/" + day + ".txt";
            
            try
            {
                return File.ReadAllLines(dataPath);
            }
            catch
            {
                AOCTools.Log("File " + day + " not found!");
                return Array.Empty<string>();
            }

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
