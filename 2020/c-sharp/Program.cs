using System;
using System.IO;

namespace AOC2020
{
    class Program
    {
        static void Main(string[] args)
        {
            string test = File.ReadAllText("../input/01");

            Day01.Run(test);
        }
    }
}
