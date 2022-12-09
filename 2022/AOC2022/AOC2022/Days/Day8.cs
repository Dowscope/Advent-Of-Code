using AOC2022.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2022.Days
{
    internal class Day8 : Day
    {
        private int[,] _grid;
        private bool[,] _visibility;
        public Day8(string day) : base(day)
        {
            
        }

        public override void OnStart()
        {
            _grid = new int[data.Length, data[0].Length];
            _visibility = new bool[data.Length, data[0].Length];

            for (int i = 0; i < data.Length; i++)
            {
                for (int j = 0; j < data[i].Length; j++)
                {
                    _grid[i, j] = Int32.Parse(data[i][j].ToString());
                    _visibility[i, j] = false;
                }
            }
        }
        public override void Part1()
        {
            for (int i = 0; i < _grid.GetLength(0); i++)
            {
                for (int j = 0; j < _grid.GetLength(1); j++)
                {
                    if (i > 0 && i < _grid.GetLength(1) - 1 && j > 0 && j < _grid.GetLength(1) - 1)
                    {
                        AOCTools.LogMore(_grid[i, j] + " ");

                        if (_grid[i-1, j] )
                    }
                }
            }
        }

        public override void Part2()
        {
        }

    }
}
