using AOC2022.Utils;

namespace AOC2022.Days
{
    internal class Day5 : Day
    {
        public Day5() 
        {
            AOCTools.Log("AOC2022 - Day 5");
            ReadData("Day5");
            if (data.Length != 0)
            {
                Part1();
                Part2();
            }
            else
            {
                AOCTools.Log("Data file empty");
            }
        }

        public override void Part1()
        {
            Dictionary<int, Stack<string>> stacks = new Dictionary<int, Stack<string>>();
            bool isInstructions = false;
            int stackedColumns = 0;

            for (int i = 0; i < data.Length; i++ )
            {
                var line = data[i];

                if (!isInstructions)
                {
                    if (line == "")
                    {
                        isInstructions = true;
                        for (int j = i - 1; j >= 0; j--)
                        {
                            var row = data[j].Split(',');
                            if (j == i - 1)
                            {
                                stackedColumns = row.Length;
                                continue;
                            }
                            for (int k = 1; k <= stackedColumns; k++) 
                            {
                                var c = row[k-1].Replace("[", "").Replace("]","").Replace(" ", "");

                                if (c == "" || c == " ")
                                {
                                    continue;
                                }

                                Stack<string> value = new Stack<string>();
                                if (stacks.TryGetValue(k, out value))
                                {
                                    stacks[k].Push(c);
                                }
                                else
                                {
                                    Stack<string> v = new Stack<string>();
                                    v.Push(c);
                                    stacks.Add(k, v);
                                }
                            }
                        }
                        continue;
                    }


                }
                else
                {
                    string[] commands = line.Split();

                    int quanity = Int32.Parse(commands[1]);
                    int from = Int32.Parse(commands[3]);
                    int to = Int32.Parse(commands[5]);

                    for (int j = 0; j < quanity; j++)
                    {
                        string toMove = stacks[from].Pop();
                        stacks[to].Push(toMove);
                    }
                }
            }

            AOCTools.Log("\nPart 1");
            foreach (var result in stacks.Values)
            {
                AOCTools.LogMore(result.Peek());
            }
            AOCTools.LogMore("\n");
        }

        public override void Part2()
        {
            Dictionary<int, Stack<string>> stacks = new Dictionary<int, Stack<string>>();
            bool isInstructions = false;
            int stackedColumns = 0;

            for (int i = 0; i < data.Length; i++)
            {
                var line = data[i];

                if (!isInstructions)
                {
                    if (line == "")
                    {
                        isInstructions = true;
                        for (int j = i - 1; j >= 0; j--)
                        {
                            var row = data[j].Split(',');
                            if (j == i - 1)
                            {
                                stackedColumns = row.Length;
                                continue;
                            }
                            for (int k = 1; k <= stackedColumns; k++)
                            {
                                var c = row[k - 1].Replace("[", "").Replace("]", "").Replace(" ", "");

                                if (c == "" || c == " ")
                                {
                                    continue;
                                }

                                Stack<string> value = new Stack<string>();
                                if (stacks.TryGetValue(k, out value))
                                {
                                    stacks[k].Push(c);
                                }
                                else
                                {
                                    Stack<string> v = new Stack<string>();
                                    v.Push(c);
                                    stacks.Add(k, v);
                                }
                            }
                        }
                        continue;
                    }


                }
                else
                {
                    string[] commands = line.Split();

                    int quanity = Int32.Parse(commands[1]);
                    int from = Int32.Parse(commands[3]);
                    int to = Int32.Parse(commands[5]);

                    string toMove = ""; 
                    for (int j = 0; j < quanity; j++)
                    {
                        toMove += stacks[from].Pop();
                    }

                    char[] ch = toMove.ToCharArray();
                    Array.Reverse(ch);

                    foreach (char c in ch)
                    {
                        stacks[to].Push(c.ToString());
                    }
                }
            }

            AOCTools.Log("\nPart 2");
            foreach (var result in stacks.Values)
            {
                AOCTools.LogMore(result.Peek());
            }
            AOCTools.LogMore("\n");
        }
    }
}
