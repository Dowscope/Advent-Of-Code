

namespace AOC2022.Utils
{
    internal class Folder
    {
        private List<Folder> _folders;
        private List<string[]> _files;

        public long GetTotalFileSize 
        { 
            get
            {
                long total = 0;
                foreach (var file in _files)
                {
                    total += long.Parse(file[1]);
                }
                return total;
            } 
        }

        public Folder(string name)
        {

        }

        public void AddFile(string name, long size)
        {
            string[] s = {name, size };
            _files.Add(new[] { name, size });
        }
    }
}
