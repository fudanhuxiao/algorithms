class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0)+1
        maxFreq = max(counter.values())
        mostFreqTasks = 0
        for task in counter:
            if counter[task] == maxFreq:
                mostFreqTasks += 1
        return max((maxFreq-1)*(n+1)+mostFreqTasks, len(tasks))
        
                
