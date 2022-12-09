

namespace AOC2022.Utils
{
    internal class Folder
    {
        private List<string[]> _files;

        public List<Folder> Folders { get; private set; }
        public string Name { get; set; }
        public int Level { get; set; }
        public Folder Parent { get; set; }
        public long TotalFileSize { get; set; }

        public Folder(string name, int level, Folder? parent = null)
        {
            Name = name;
            Level = level;
            Parent = parent;
        }

        public void AddFile(string name, string size)
        {
            if (_files == null) _files = new List<string[]>();
            _files.Add(new[] { name, size });
            TotalFileSize += long.Parse(size);
        }

        public void AddFolder(string name)
        {
            if (Folders == null) Folders = new List<Folder>();
            Folders.Add(new Folder(name, Level + 1, this));
        }

        public Folder? GetFolder(string name)
        {
            if (Folders != null)
            {
                foreach(var f in Folders)
                {
                    if(f.Name == name)
                    {
                        return f;
                    }
                }
            }
            return null;
        }

        public bool Exists(string type, string name)
        {
            if (type == "d" && Folders != null)
            {
                foreach (var f in Folders)
                {
                    if (f.Name == name)
                    {
                        return true;
                    }
                }
                return false;
            }
            else if (type == "f" && _files != null)
            {
                foreach (var f in _files)
                {
                    if (f[0] == name)
                    {
                        return true;
                    }
                }
                return false;
            }
            return false;
        }
    }
}
