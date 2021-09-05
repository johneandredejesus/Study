using System.Collections.Generic;

namespace Builder
{
    public class MealBox : IMeal
    {
        public int Quantity
        {
            get
            {
                int quantity = 0;

                this.meals.ForEach((IMeal meal) => quantity += meal.Quantity);

                return quantity;
            }
        }
        public double Price
        {
            get
            {
                double price = 0;

                this.meals.ForEach((IMeal meal) => price += meal.Price);

                return price;
            }
        }

        private List<IMeal> meals;

        public MealBox()
        {
            this.meals = new List<IMeal>();
        }
        public void Add(params IMeal[] meals)
        {
            foreach (IMeal item in meals)
                this.meals.Add(item);
        }
    }
}