'''
Python dictionary containing 1 dictionary for each node.
The internal dictionary contains the children of the outer node, as well as the associated weights. 
Nodes: edge={child node: distance} 
'''
star_galactica = { "Ajan Kloss": {"Bahu": 23, "Bothawui": 17, "Bespin and Hoth": 30},
                   "Bahu": {"Ach-To" : 9, "Endor and Kef Bir": 6},
                   "Bothawui": {"Cantanica": 18, "Kessel": 8},
                   "Bespin and Hoth": {"Crait": 8, "D'Qar": 9},
                   "Ach-To": {"Cantanica": 33},
                   "Endor and Kef Bir": {"Sullust": 15, "Ring of Kafrene": 8},
                   "D'Qar": {"Sullust": 3, "Naboo": 3},
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

def ucs(graph, origin, target):
  visited = []
  # copy = graph.copy()
  previous = None
  list_of_next_node = [(0, origin)]
  visited.append(origin)
  if origin == target:
    print("found",origin)
    quit()
  res = None
  while res != target:
    list_of_next_node = sorted(list_of_next_node)
    s = list_of_next_node[0]
    list_of_next_node.pop(0)
    print("s:",s,graph[s[1]])
    previous = s[0]
    for neighbour in graph[s[1]]:
      list_of_next_node.append((graph[s[1]][neighbour]+previous, neighbour))
    s = sorted(list_of_next_node)
    print("S:",s,target)
    res = s[0][1]
    print("Res: ",res)
  print("found",res)

def best_path_calculator(graph, src):
  queue = [src]
  minDistances = {v: float("inf") for v in graph}
  minDistances[src] = 0
  predecessor = {}

  while queue:
    print("A",minDistances, predecessor)
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
  print("B",minDistances, predecessor)
  print("Current node: ", currentNode)
  while currentNode != origin:
    if currentNode not in predecessor:
      print("Path not reachable")
      break
    else:
      path.insert(0, currentNode)
      currentNode = predecessor[currentNode]
      print("Curr",currentNode)
  path.insert(0, origin)

  if dest in minDistances and minDistances[dest] != float("inf"):
    print('Found: ' + dest, ",in the shortest path of " + str(minDistances[dest]),
          "and the path is ", str(path))
  else:
    print("No possible path to that planet")

def main():
  '''///////////////////////////////////////// Execution Area ////////////////////////////////////////////'''
  dfs(set(), star_galactica, 'Ajan Kloss', "Sullust", False)
  uniform_cost_search(star_galactica, 'Ajan Kloss', "Sullust")
  ucs(star_galactica, 'Ajan Kloss', "Sullust") # path for ucs | (sort not by name) | no possible path? || rewrite 

if __name__ == '__main__':
  main()
