namespace Builder
{
    public interface IMealBoxBuilder
    {
        IMealBoxBuilder MakeMeal();
        void Reset();
    }
}