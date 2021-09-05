namespace Builder
{
    public abstract class Meal : IMeal
    {
        int quantity;
        double price;
        public int Quantity => this.quantity;
        public double Price => price;
        public Meal(int quantity, double price)
        {
            this.quantity = quantity;
            this.price = price;
        }
    }
}