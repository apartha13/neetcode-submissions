class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        res = []

        if not tokens:
            return 0

        for token in tokens:
            if token in operators:
                sec = int(res.pop())
                fir = int(res.pop())
                tot = 0

                if token == '+':
                    tot += fir + sec
                if token == '*':
                    tot += fir * sec
                if token == '/':
                    tot += fir / sec
                if token == '-':
                    tot += fir - sec
                
                res.append(tot)
            else:
                res.append(token)
        
        return int(res.pop())