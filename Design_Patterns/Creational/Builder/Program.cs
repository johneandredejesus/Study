using System;
using System.Collections.Generic;

namespace Builder
{

    class Program
    {
        static void Main(string[] args)
        {
            MealBoxBuilder box = new MealBoxBuilder();

            box.MakeMeal().MakeMeal().MakeMeal();

            Console.WriteLine(box.Price);
            
            Console.WriteLine(box.Quantity);
        }
    }
}
