public class Solution
{
    public string IntToRoman(int num)
    {
        return num switch
        {
            >= 1000 => "M" + IntToRoman(num - 1000),
            >= 900 and <= 999 => "CM" + IntToRoman(num - 900),
            >= 500 and <= 899 => "D" + IntToRoman(num - 500),
            >= 400 and <= 499 => "CD" + IntToRoman(num - 400),
            >= 100 and <= 399 => "C" + IntToRoman(num - 100),
            >= 90 and <= 99 => "XC" + IntToRoman(num - 90),
            >= 50 and <= 89 => "L" + IntToRoman(num - 50),
            >= 40 and <= 49 => "XL" + IntToRoman(num - 40),
            >= 10 and <= 39 => "X" + IntToRoman(num - 10),
            9 => "IX" + IntToRoman(num - 9),
            >= 5 and <= 8 => "V" + IntToRoman(num - 5),
            4 => "IV" + IntToRoman(num - 4),
            >= 1 and <= 3 => "I" + IntToRoman(num - 1),
            _ => ""
        };
    }
}