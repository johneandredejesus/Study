using System.Collections.Generic;

namespace Singleton
{
     public class ClientsSingleton
    {
       private  static ClientsSingleton instance; 
       
       private readonly List<IClient> clients;
       private ClientsSingleton()
       {
            this.clients = new List<IClient>();
       }

       public static ClientsSingleton Instance
       {
           get =>  instance == null ? instance = new ClientsSingleton(): instance;
       }

       public void Add(IClient client)
       {
           this.clients.Add(client);
       }

       public void Remove(IClient client)
       {
           this.clients.Remove(client);
       }
       
       public List<IClient> Show()
       {
           return this.clients;
       }
    }
}