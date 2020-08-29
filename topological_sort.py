from collections import deque
def topological_sort(vertices, edges):
      sortedOrder = []
      # TODO: Write your code here
      if vertices <= 0:
            return sortedOrder
      # 1. use dictionaries to store the graph
      indegree = {i:0 for i in range(vertices)}
      graph = {i:[] for i in range(vertices)}

      # 2. build the dictionaries
      for parent, child in edges:
            indegree[child] += 1
            graph[parent].append(child)
      
      # 3. find all the sources
      sources = deque()
      for key in indegree:
            if indegree[key] == 0:
                  sources.append(key)
      
      # 4. bfs, add all the vertices in sortedOrder
      while sources:
            vertice = sources.popleft()
            sortedOrder.append(vertice)
            for child in graph[vertice]:
                  indegree[child] -= 1
                  if indegree[child] == 0:
                        sources.append(child)
      return sortedOrder
