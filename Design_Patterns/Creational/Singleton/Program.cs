using System;

namespace Singleton
{
    
    class Program
    {
        static void Main(string[] args)
        {
          
           ClientsSingleton instence1 = ClientsSingleton.Instance;
           
           instence1.Add(new Client("Fernada", 25));
           instence1.Add(new Client("Lucas", 20));
           instence1.Add(new Client("Ana", 22));
           instence1.Add(new Client("Matheus", 19));
           instence1.Add(new Client("Bruna", 23));

           instence1.Show().ForEach((client)=>Console.WriteLine($"Name: {client.Name} Age: {client.Age}"));
            
           ClientsSingleton instence2 = ClientsSingleton.Instance;

           Console.WriteLine(instence1 == instence2);
        }
    }
}
