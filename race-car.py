class Solution:
    def racecar(self, target: int) -> int:
        # move, position, speed
        queue = deque([(0, 0, 1)])
        while queue:
            move, pos, speed = queue.popleft()
            if pos == target:
                return move
            queue.append((move+1, pos+speed, speed*2))
            if (speed > 0 and pos+speed > target) or (speed < 0 and pos+speed < target):
                queue.append((move+1, pos, -1 if speed > 0 else 1))
        
