using System;
					
public class LongestCommonSubsequence
{
	public static string longestCommonSubsequence(string s1, string s2){
    // Create a length maxtrix with the first row and column set to all 0s
		int[,] longestCommonSubsequenceMatrix = new int[s1.Length + 1,s2.Length + 1];
		for(int i = 1; i < s1.Length + 1; i++){
			for(int j = 1; j <  s2.Length + 1; j ++){
				if(s1[i - 1] == s2[j - 1]){
					longestCommonSubsequenceMatrix[i,j] = longestCommonSubsequenceMatrix[i - 1, j - 1] + 1;
				}
				else{
					longestCommonSubsequenceMatrix[i,j] = Math.Max(longestCommonSubsequenceMatrix[i-1,j], longestCommonSubsequenceMatrix[i,j-1]);
				}
			}
		}
		
		char[] longestCommonSubsequence = new char[longestCommonSubsequenceMatrix[s1.Length,s2.Length]];
		Console.WriteLine(longestCommonSubsequenceMatrix[s1.Length,s2.Length]);
		
		int row = s1.Length;
		int col = s2.Length;
		int pointer = longestCommonSubsequenceMatrix[s1.Length,s2.Length] - 1;
		
		while(row > 0 && col > 0)
		{
			if(s1[row - 1] == s2[col - 1])
			{
				longestCommonSubsequence[pointer] = s1[row - 1];
				row -= 1;
				col -= 1;
				pointer -= 1;
			}
			else
			{
				if(longestCommonSubsequenceMatrix[row - 1, col] > longestCommonSubsequenceMatrix[row, col - 1])
				{
					row -= 1;
				}
				else{
					col -= 1;
				}
				
			}
		}
		return new string(longestCommonSubsequence);
	}
	public static void Main()
	{
		Console.WriteLine("Please input the first string:");
		String s1  = Console.ReadLine();
		Console.WriteLine("Please input the second string:");
		String s2  = Console.ReadLine();
		Console.WriteLine(String.Format("The longest common subsequence of {0} and {1} is {2}.", s1, s2, longestCommonSubsequence(s1,s2)));
	}
}
