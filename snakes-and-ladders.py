class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = collections.deque()
        queue.append(1)
        distances = {1:0}
        while queue:
            curr = queue.popleft()
            for i in range(curr+1, curr+7):
                r, c = (i-1)//n, (i-1)%n
                nxt = board[n-1-r][c if r%2==0 else n-1-c]
                if nxt != -1:
                    i = nxt
                if i == n*n:
                    return distances[curr]+1
                if i not in distances:
                    distances[i] = distances[curr]+1
                    queue.append(i)
        return -1
