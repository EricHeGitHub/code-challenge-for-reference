using System;
// find the longest common substring of s1 and s2			
public class LongestCommonSubstring
{
	public static string longestCommonString(string s1, string s2){
		int[,] longestCommonStringMatrix = new int[s1.Length + 1,s2.Length + 1];
		int maxLen = 0;
		int position = 0;
		for(int i = 1; i < s1.Length + 1; i++){
			for(int j = 1; j <  s2.Length + 1; j ++){
				if(s1[i - 1] == s2[j - 1]){
					longestCommonStringMatrix[i,j] = longestCommonStringMatrix[i - 1, j - 1] + 1;
					if(longestCommonStringMatrix[i,j] > maxLen){
						maxLen = longestCommonStringMatrix[i,j];
						position = i - 1;
					}
				}
			}
		}
		string longestCommonString = s1.Substring(position - maxLen + 1, maxLen);
		
		return longestCommonString;
	}
	public static void Main()
	{
		Console.WriteLine("Please input the first string:");
		String s1  = Console.ReadLine();
		Console.WriteLine("Please input the second string:");
		String s2  = Console.ReadLine();
		Console.WriteLine(String.Format("The longest common string of {0} and {1} is {2}.", s1, s2, longestCommonString(s1,s2)));
	}
}
