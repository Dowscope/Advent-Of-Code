using AOC2022.Utils;

namespace AOC2022.Days
{
    internal class Day7 : Day
    {
        public Day7(string day) : base(day)
        {
        }

        public override void Part1()
        {
            int level = 0;   // 0 is root level
            Folder currentFolder = new Folder("/", 0);

            foreach (var line in data)
            {
                var words = line.Split();

                if (words[0] == "$")
                {
                    if (words[1] == "cd")
                    {
                        if (words[2] == "/")
                        {
                            currentFolder = _ReturnToRoot(currentFolder, level);
                            level = 0;
                        }
                        else if (words[2] == "..")
                        {
                            if (level > 0 && currentFolder != null)
                            {
                                currentFolder = currentFolder.Parent;
                                level--;
                            }
                        }
                        else
                        {
                            currentFolder = currentFolder.GetFolder(words[2]);
                            if (currentFolder == null)
                            {
                                AOCTools.Log("Invalid Folder: " + words[2]);
                                break;
                            }
                            level++;
                        }
                    }
                }
                else if (words[0] == "dir")
                {
                    if (currentFolder != null && !currentFolder.Exists("d", words[1]))
                    {
                        currentFolder.AddFolder(words[1]);
                    }
                }
                else
                {
                    if (currentFolder != null && !currentFolder.Exists("f", words[1]))
                    {
                        currentFolder.AddFile(words[1], words[0]);
                    }
                }
            }

            currentFolder = _ReturnToRoot(currentFolder, level);
            level = 0;
            _TotalSizeOfFolderUpdate(currentFolder);
            _GetTotalSizes(currentFolder);
            long total = 0;
            foreach (var t in _totals)
            {
                total += t;
            }
            AOCTools.Log("Total File Size: " + total);
        }

        public override void Part2()
        {

        }

        private void _TotalSizeOfFolderUpdate(Folder current)
        {
            if (current.Folders != null)
            {
                foreach (var f in current.Folders)
                {
                    _TotalSizeOfFolderUpdate(f);
                }
            }

            if (current.Parent != null)
            {
                AOCTools.Log("Adding " + current.TotalFileSize + " to folder " + current.Parent.Name);
                current.Parent.TotalFileSize += current.TotalFileSize;
            }
        }

        private List<long> _totals = new List<long>();
        private void _GetTotalSizes(Folder current)
        {
            if (current.TotalFileSize > 100000 && current.Folders != null)
            {
                foreach (var f in current.Folders)
                {
                    _GetTotalSizes(f);
                }
            }

            if (current.TotalFileSize <= 100000)
            {
                _totals.Add(current.TotalFileSize);
            }
        }

        private Folder _ReturnToRoot(Folder current, int level)
        {
            while (level > 0)
            {
                current = current.Parent;
                level--;
            }

            return current;
        }
    }
}
