star_galactica = { "Ajan Kloss": {"Bahu": 15, "Bothawui": 11, "Bespin and Hoth": 20},
                   "Bahu": {"Ach-To" : 6, "Endor and Kef Bir": 4},
                   "Bothawui": {"Cantanica": 12, "Kessel": 5},
                   "Bespin and Hoth": {"Crait": 5, "D'Qar": 6},
                   "Ach-To": {"Cantanica": 22},
                   "Endor and Kef Bir": {"Sullust": 10, "Ring of Kafrene": 5},
                   "D'Qar": {"Sullust": 2, "Naboo": 2},
                   "Cantanica": {},
                   "Sullust": {},
                   "Ring of Kafrene": {},
                   "Kessel": {},
                   "Crait": {},
                   "Naboo": {}
                   }


def dfs(visited, graph, origin, target, found):
    global temp_found
    temp_found = found
    visited = set()
    if temp_found:
        return None
    if origin not in visited:
        print ("->", origin)
        visited.add(origin)
        if origin in target:
          print(target, "Found")
          temp_found = True
        for neighbour in graph[origin]:
            dfs(visited, graph, neighbour, target, temp_found)

# def ucs(graph, origin, target):
#   list_of_next_node = [(0, origin)]
#   visited.append(origin)
#   if origin == target:
#     quit()
#   counter = 1
#   while True:
#     counter += 1
#     list_of_next_node = sorted(list_of_next_node)
#     s = list_of_next_node[0]
#     list_of_next_node.pop(0)
#     print(graph[s[1]])
#     for neighbour in graph[s[1]]:
#       list_of_next_node.append((graph[s[1]][neighbour], neighbour))
#     s = sorted(list_of_next_node)
#     print(s)
#     if counter == 4:
#       break

# ucs(star_galactica, 'Ajan Kloss', "whatever")
# def bfs(visited, graph, node):
#     print(visualize_tree())
#     visited.append(node)
#     queue.append(node)
#     while queue:
#         s = queue.pop(0)
#         print("bfs",s)
#         if s == target:
#             print("Found: ",s)
#             break
#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)

def best_path_calculator(graph, src):
  queue = [src]
  minDistances = {v: float("inf") for v in graph}
  minDistances[src] = 0
  predecessor = {}

  while queue:
    currentNode = queue.pop(0)
    for neighbor in graph[currentNode]:
      newDist = minDistances[currentNode] + graph[currentNode][neighbor]
      if newDist < minDistances[neighbor]:
        minDistances[neighbor] = min(newDist, minDistances[neighbor])
        queue.append(neighbor)
        predecessor[neighbor] = currentNode

  return minDistances, predecessor

def uniform_cost_search(graph, origin, dest):
  minDistances, predecessor = best_path_calculator(graph, origin)
  path = []
  currentNode = dest
  while currentNode != origin:
    if currentNode not in predecessor:
      print("Path not reachable")
      break
    else:
      path.insert(0, currentNode)
      currentNode = predecessor[currentNode]
  path.insert(0, origin)

  if dest in minDistances and minDistances[dest] != float("inf"):
    print('Found: ' + dest, ",in the shortest path of " + str(minDistances[dest]),
          "and the path is ", str(path))
  else:
    print("No possible path to that planet")

# ///////////////////////////////////////////////// Execution Area /////////////////////////////////////////////

found = False
visited = set()
dfs(visited, star_galactica, 'Ajan Kloss', "Sullust", False)
uniform_cost_search(star_galactica, 'Ajan Kloss', "Sullust")