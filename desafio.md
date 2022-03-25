using System;

public class Storm
{
    public double EyeRadius { get; protected set; }
    public Tuple<double, double> EyePosition { get; protected set; }
    
    public bool IsInEyeOfTheStorm(Tuple<double, double> position)
    {
        double distance = Math.Sqrt(Math.Pow(position.Item1 - EyePosition.Item1, 2) +
                                    Math.Pow(position.Item2 - EyePosition.Item2, 2));
        return distance < EyeRadius;
    }
    
    public Storm(double eyeRadius, Tuple<double, double> eyePosition)
    {
        this.EyeRadius = eyeRadius;
        this.EyePosition = eyePosition;
    }
}

public class RainStorm : Storm
{
        
    public RainStorm(double eyeRadius, Tuple<double, double> eyePosition) : base(eyeRadius, eyePosition)
    {
    }
   
    
    public double AmountOfRain()
    {
        return EyeRadius * 20;
    }
}

public class SnowStorm : Storm
{
   
    public double AmountOfSnow { get; private set; }
    
    public SnowStorm(double eyeRadius, Tuple<double, double> eyePosition, double amountOfSnow) : base(eyeRadius, eyePosition)
    
    {
        this.AmountOfSnow = amountOfSnow;
    }    
   
}



using System;

public class RemoveRepetitions
{
    public static string Transform(string input)
    {
      string result = input[0].ToString();
          
      for (int i = 1; i < input.Length; i++)
      {
          if(input[i] == input[i - 1])
          {
              continue;
          }
          else
          {
              result = result + input[i];
          }
      }
      return result;
    }

    public static void Main(string[] args)
    {
        Console.WriteLine(RemoveRepetitions.Transform("abbcbbb"));
    }
}