using System.Collections;

namespace _2023;

public interface IDay
{
    Dictionary<int,string> Content {get; set;}
    Dictionary<int,string> Results {get; set;}
    void LoadContent(string filePath, int index);
    void DisplayResults();

    void Testing();
    void PartOne();
    void PartTwo();
}
