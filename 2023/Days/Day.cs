using System.Collections;

namespace _2023;

public abstract class Day : IDay
{
    public Dictionary<int,string> Content { get; set; }
    public Dictionary<int,string> Results { get; set; }

    public Day()
    {
        Content = new Dictionary<int,string>();
        Results = new Dictionary<int,string>();
    }

    public void LoadContent(string filePath, int index)
    {
        Console.Write($"Loading in {filePath}... ");
        try
        {
          Content[index] = File.ReadAllText(filePath);
          Console.WriteLine("Successful");
        }
        catch (Exception ex)
        {
          Console.WriteLine($"Failed.\nError loading file: {ex.Message}");
          throw;
        }
    }

    public void DisplayResults()
    {
        if (Results != null && Results.Count > 0)
        {
            foreach (var r in Results)
            {
                switch (r.Key)
                {
                    case 0:
                        Console.WriteLine($"Testing Result: {r.Value}");
                        break;
                    case 1:
                        Console.WriteLine($"Part 1 Result: {r.Value}");
                        break;
                    case 2:
                        Console.WriteLine($"Part 2 Result: {r.Value}");
                        break;
                    default:
                        Console.WriteLine($"Part {r.Key} Result: {r.Value}");
                        break;
                }
            }
        }
        else
        {
          Console.WriteLine("No Results");
        }
    }

    public virtual void Testing() {
        Console.WriteLine("Testing");
    }

    public virtual void PartOne() {
        Console.WriteLine("Testing");
    }

    public virtual void PartTwo() {
        Console.WriteLine("Testing");
    }
}
