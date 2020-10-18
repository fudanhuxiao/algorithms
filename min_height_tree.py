from collections import deque
def find_trees(nodes, edges):
      # TODO: Write your code here
      graph = [[] for _ in range(nodes)]
      indegree = [0 for _ in range(nodes)]
      for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)
            indegree[a] += 1
            indegree[b] += 1
      leaves = deque()
      for i in range(nodes):
            if indegree[i] == 1:
                  leaves.append(i)
      count_leaves = 0
      while leaves:
            n = len(leaves)
            count_leaves += n
            if nodes == count_leaves:
                  return list(leaves)
            for _ in range(n):
                  node = leaves.popleft()
                  for child in graph[node]:
                        indegree[child] -= 1
                        if indegree[child] == 1:
                              leaves.append(child)
      return []


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()
