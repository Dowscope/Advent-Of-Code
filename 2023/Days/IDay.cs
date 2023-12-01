using System.Collections;

namespace _2023;

public interface IDay
{
    Dictionary<int,string[]> Content {get; set;}
    Dictionary<int,string> Results {get; set;}

    void LoadContent(string filePath, int index);
    void DisplayContent(int index);
    void DisplayResults();

    void Run(int part);
    void PartOne(string[] data, out string answer);
    void PartTwo(string[] data, out string answer);
}
