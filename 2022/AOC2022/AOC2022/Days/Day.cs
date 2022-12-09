

using AOC2022.Utils;

namespace AOC2022.Days
{
    internal abstract class Day
    {
        public string[] data;

        public Day(string day)
        {
            AOCTools.Log("AOC2022 - " + day);
            ReadData(day);
            if (data != null && data.Length != 0)
            {
                OnStart();
                Part1();
                Part2();
            }
            else
            {
                AOCTools.Log("Data file empty");
            }
        }

        public void ReadData(string day)
        {
            data = AOCTools.GetData(day);
        }
        public virtual void OnStart()
        {

        }

        public abstract void Part1();
        public abstract void Part2();
    }
}
