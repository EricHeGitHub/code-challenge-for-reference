
public class Palindromic {
    // Check if a string is palindromic
    public bool isPalindromic(string s){ 
        if(s == "" || s.Length == 1){
            return true;
        }
        Stack myStack = new Stack();
        if(s.Length % 2 != 0){
            for(int i = 0; i < s.Length/2; i++){
                myStack.Push(s[i]);
            }
            for(int i = s.Length/2 + 1; i < s.Length; i++){
                if(s[i] == (char) myStack.Peek()){
                    myStack.Pop();
                }
            }
            
            if(myStack.Count == 0){
                return true;
            }
            else{
                return false;
            }
            
        }
        
        else if(s.Length % 2 == 0){
            for(int i = 0; i < s.Length/2; i++){
                myStack.Push(s[i]);
            }
            for(int i = s.Length/2; i < s.Length; i++){
                if(s[i] == (char) myStack.Peek()){
                    myStack.Pop();
                }
            }
            
            if(myStack.Count == 0){
                return true;
            }
            else{
                return false;
            }
            
        }
        
        return false;
    }
}
