
class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        
        for char in s:
            if char in myMap:
                if stack and myMap[char] == stack.pop():
                    continue
                else:
                    return False
            stack.append(char)
        
        if stack:
            return False
        return True

                
        