class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
            
        # Mapping of closing brackets to opening brackets
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in close_to_open:          # It's a closing bracket
                if not stack or stack[-1] != close_to_open[char]:
                    return False
                stack.pop()                    # Valid pair found
            else:                              # It's an opening bracket
                stack.append(char)
        
        # Stack should be empty if all brackets are properly closed
        return len(stack) == 0