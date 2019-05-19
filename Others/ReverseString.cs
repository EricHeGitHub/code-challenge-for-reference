
public class ReverseString {    
    public string reverseString(string s){
        if(s.Length == 0 ||s.Length == 1){
            return s;
        }
        char tail = s[s.Length - 1];
        
        string result = tail.ToString() + reverseString(s.Substring(0, s.Length - 1));
        
        return result;
        
    }
}
