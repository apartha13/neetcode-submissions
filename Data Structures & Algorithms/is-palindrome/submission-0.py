import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate (str.maketrans('', '', string.punctuation))
        s = s.lower()
        arrFor = []
        arrBac = []
        for x in s:
            if x != ' ':
                arrFor.extend(x)
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                arrBac.extend(s[i])
  
        if arrFor == arrBac:
            return True
        return False