
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
                if stack and stack.pop() == myMap[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        return False
                

        