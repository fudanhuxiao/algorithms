def print_orders(tasks, prerequisites):
  graph = [[] for _ in range(tasks)]
  indegree = [0 for _ in range(tasks)]
  for parent, child in prerequisites:
    graph[parent].append(child)
    indegree[child] += 1
  current = set()
  for i in range(tasks):
    if indegree[i] == 0:
      current.add(i)
  print_all(current, [], indegree, graph)

def print_all(current, path, indegree, graph):
  if len(path) == len(indegree):
    print(path)
    return
  for task in current:
    path.append(task)
    new = set(current)
    new.remove(task)
    for child in graph[task]:
      indegree[child] -= 1
      if indegree[child] == 0:
        new.add(child)
    print_all(new, path, indegree, graph)
    path.pop()
    for child in graph[task]:
      indegree[child] += 1
      
def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
