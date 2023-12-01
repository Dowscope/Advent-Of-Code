using System.Text.RegularExpressions;
using System.Linq;

namespace _2023;

public class Day1 : Day
{
    public override void Run(int part)
    {
        base.Run(part);

        
        if (Content[part] != null)
        {
            string res;
            PartOne(Content[part], out res);
            Results[part] = res;
        }
        else
        {
            Results[part] = $"Error: No content for testing - {part}";
        }
    }

    public override void PartOne(string[] data, out string answer)
    {
        base.PartOne(data, out answer);

        long r = 0;
        foreach (string c in data)
        {
            var matches = Regex.Matches(c, @"\d");

            if (matches.Count > 0)
            {
                string first = matches[0].Value;
                string last = matches[matches.Count - 1].Value;
                string res = first + last;
                r += long.Parse(res);
            }
        }
        answer = $"{r}";
    }

    public override void PartTwo(string[] data, out string answer)
    {
        base.PartOne(data, out answer);

        
    }
}
