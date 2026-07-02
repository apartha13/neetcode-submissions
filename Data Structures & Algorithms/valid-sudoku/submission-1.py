class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        ind = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                index = (r // 3, c // 3)
                if (val in cols[c]) or (val in rows[r]) or (val in ind[index]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                ind[index].add(val)

        return True