class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowercase = s.lower()
        s_connected = s_lowercase.replace(" ", "")
        arr = [char for char in s_connected if char.isalnum()]
        
        end_pointer = len(arr)-1
        start_pointer = 0
        
        while start_pointer < end_pointer:
            
            if arr[start_pointer] != arr[end_pointer]:
                return False  
                      
            start_pointer+=1
            end_pointer -=1
            
            
        return True