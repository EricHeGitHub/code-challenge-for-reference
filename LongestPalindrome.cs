//Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

//Example 1
//Input: "babad"
//Output: "bab"
//Note: "aba" is also a valid answer.

//Example 2
//Input: "cbbd"
//Output: "bb"


public class LongestPalindrome {
    public string FindLongestPalindrome(string s) {
        if(s == "")
        {
            return "";
        }
        int index = 0;
        int maxLen = 0;
        int leftPointer;
        int rightPointer;
        bool betweenCharMax = false;
        for(int i = 0 ; i < 2 * s.Length - 1 ; i++){
            int len = 0;
            bool betweenChar = false;
            if(i % 2 == 0) {
                len += 1;
                leftPointer = i / 2 - 1;
                rightPointer = i / 2 + 1;
            }
            else{              
                leftPointer = i / 2;
                rightPointer = i / 2 + 1;
                betweenChar = true;
            }
            
            while(leftPointer >= 0 && rightPointer <= s.Length - 1){
                    if(s[leftPointer] == s[rightPointer]){
                        len += 2;
                        leftPointer -= 1;
                        rightPointer += 1;
                    }
                    else{
                        break;
                    }
                    
                } 
                //Console.WriteLine(i + " " + i/2 + " " + len);
                if(maxLen < len){
                    index = i / 2;
                    maxLen = len;
                    betweenCharMax = betweenChar;
                }
        } 
        //Console.WriteLine(index + " " + maxLen);
        //abccba
        if(betweenCharMax){
            return s.Substring(index + 1 - maxLen/2, maxLen);
        }
        //abcdcba
        else{
           return s.Substring(index + 1 - (maxLen + 1)/2, maxLen); 
        }
    }
}
