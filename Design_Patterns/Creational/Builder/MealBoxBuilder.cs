namespace Builder
{
    public class MealBoxBuilder : IMealBoxBuilder
    {
        MealBox mealBox;

        public MealBox MealBox => this.mealBox;
        public MealBoxBuilder()
        {
            this.mealBox = new MealBox();
        }
        public void Reset()
        {
            this.mealBox = new MealBox();
        }
        public IMealBoxBuilder MakeMeal()
        {
            this.mealBox.Add(new Pasta(1, 2.40), new Bean(1, 2.00), new Rice(1, 1.50));

            return this;
        }

        public double Price => this.mealBox.Price;

        public double Quantity => this.mealBox.Quantity;

    }
}