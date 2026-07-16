class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastLength = 0
        length = 0

        for c in s:
            
            if c == " ":
                lastLength = length if length != 0 else lastLength
                length = 0
            else:
                length += 1
            
            print(c, length)
        
        return length if length != 0 else lastLength