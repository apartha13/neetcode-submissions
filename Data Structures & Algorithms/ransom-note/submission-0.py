import string

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {char: 0 for char in string.ascii_lowercase}

        for c in magazine:
            dic[c] += 1

        for c in ransomNote:
            if dic[c] == 0:
                return False
            dic[c] -= 1
        
        return True