

using AOC2022.Utils;

namespace AOC2022.Days
{
    internal abstract class Day
    {
        public string[] data;
        public void ReadData(string day)
        {
            data = AOCTools.GetData(day);
        }

        public abstract void Part1();
        public abstract void Part2();

    }
}
