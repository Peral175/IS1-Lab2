'''
Python dictionary containing 1 dictionary for each vertex.
The internal dictionary contains the children of the outer vertex, as well as the associated weights. 
Vertices: edge={child node: distance} 
'''
star_galactica = { "Ajan Kloss": {"Batuu": 23, "Bothawui": 17, "Bespin and Hoth": 30},
                   "Batuu": {"Ach-To" : 9, "Endor and Kef Bir": 6},
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
'''
ToDo
'''
heuristic_table = { "Ajan Kloss": {"Batuu": 15, "Bothawui": 11, "Bespin and Hoth": 20},
                   "Batuu": {"Ach-To" : 5, "Endor and Kef Bir": 3},
                   "Bothawui": {"Cantanica": 15, "Kessel": 4},
                   "Bespin and Hoth": {"Crait": 5, "D'Qar": 6},
                   "Ach-To": {"Cantanica": 15},
                   "Endor and Kef Bir": {"Sullust": 8, "Ring of Kafrene": 5},
                   "D'Qar": {"Sullust": 2, "Naboo": 2},
                  #  "Cantanica": {},
                  #  "Sullust": {},
                  #  "Ring of Kafrene": {},
                  #  "Kessel": {},
                  #  "Crait": {},
                  #  "Naboo": {}
                   }

def dfs(list_of_visited_nodes, graph, current_node, target):
  '''
  Desc:
    Depth First Seach algorithm -> recursively expands child nodes for each node until leaf node is reached.
  Parameters:
    list_of_visited_nodes: list = empty list to keep track of nodes expanded during algorithm execution
    graph: {node:{child_node: weight}} = tree structure composed of a nested algorithm (vertices, edges, weights)
    current_node: string = node currently being expanded -> root node for initial function call
    target: string = node that we are trying to find in the tree structure
  Return value:
    list_of_visited_nodes: list = explained above
  '''
  list_of_visited_nodes.append(current_node)  # keep track of the nodes visited
  print ("Current node:\t->", current_node) 
  if current_node == target:                  # verify if target has been found
    print("Target {target} has been found!".format(target=current_node))
    return list_of_visited_nodes              # return path of nodes visited for algorithm
  else:
    for neighbour in graph[current_node]:     # iterate through children of current node
      found = dfs(list_of_visited_nodes, graph, neighbour, target)  # recursion
      if found != None:                       # we keep track if a solution as been found in another function call
        return found

def ucs(list_of_visited_nodes, graph, root, target):
  '''
  Desc:
    Uniform Cost Search algorithm:
      -> algorithm always expands node where the total weight of the path to the node is lowest.
  Parameters:
    list_of_visited_nodes: list = empty list to keep track of nodes expanded during algorithm execution
    graph: {node:{child_node: weight}} = tree structure composed of a nested algorithm (vertices, edges, weights)
    root: string = root node of the graph
    target: string = node that we are trying to find in the tree structure
  Return value:
    list_of_visited_nodes: list = explained above
  '''
  current_node = root                               # root is first node
  sorted_list = [(0,current_node)]                  # initialize sorted list with root node and summed weight of 0
  while current_node != target:
    try:
      prev_weight, current_node = sorted_list.pop(0)# we visited node -> it can be removed from the sorted list
    except IndexError:                              # Exception -> list is empty
      return "Target {} has not been found in the graph!".format(target)
    list_of_visited_nodes.append(current_node)      # add it to list of visited nodes
    for neighbour in graph[current_node]:           # parse children of current node
      sorted_list.append((graph[current_node][neighbour] + prev_weight, neighbour)) # add child nodes to list with updated weight
    sorted_list = sorted(sorted_list)               # sort list according to lowest weight
    print ("Total weight of path: {} -- node: {}".format(prev_weight,current_node))
  print("Target {target} has been found!".format(target=current_node))
  return list_of_visited_nodes                      # return the path of visited nodes
  
# def best_path_calculator(graph, src):
#   queue = [src]
#   minDistances = {v: float("inf") for v in graph}
#   minDistances[src] = 0
#   predecessor = {}
#   while queue:
#     print("A",minDistances, predecessor)
#     currentNode = queue.pop(0)
#     for neighbor in graph[currentNode]:
#       newDist = minDistances[currentNode] + graph[currentNode][neighbor]
#       if newDist < minDistances[neighbor]:
#         minDistances[neighbor] = min(newDist, minDistances[neighbor])
#         queue.append(neighbor)
#         predecessor[neighbor] = currentNode
#   return minDistances, predecessor

# def uniform_cost_search(graph, origin, dest):
#   minDistances, predecessor = best_path_calculator(graph, origin)
#   path = []
#   currentNode = dest
#   print("B",minDistances, predecessor)
#   print("Current node: ", currentNode)
#   while currentNode != origin:
#     if currentNode not in predecessor:
#       print("Path not reachable")
#       break
#     else:
#       path.insert(0, currentNode)
#       currentNode = predecessor[currentNode]
#       print("Curr",currentNode)
#   path.insert(0, origin)
#   if dest in minDistances and minDistances[dest] != float("inf"):
#     print('Found: ' + dest, ",in the shortest path of " + str(minDistances[dest]),
#           "and the path is ", str(path))
#   else:
#     print("No possible path to that planet")

def greedy():
  pass

def a_star():
  pass

def main():
  '''///////////////////////////////////////// Execution Area ////////////////////////////////////////////'''
  
  ROOT_NODE = 'Ajan Kloss'
  TARGET_NODE = 'Sullust'
  INVALID_TARGET_NODE = 'Invalid Name'

  list_of_visited_nodes = list()
  dfs_solution = dfs(list_of_visited_nodes, star_galactica, ROOT_NODE, TARGET_NODE)
  print("Depth First Search: ",dfs_solution)
  
  list_of_visited_nodes = list()
  ucs_solution = ucs(list_of_visited_nodes, star_galactica, ROOT_NODE, TARGET_NODE)
  print("Uniform Cost Search: ", ucs_solution)

  # ucs(heuristic_table, 'Ajan Kloss', "Sullust")
  # uniform_cost_search(heuristic_table, 'Ajan Kloss', "Sullust")
  greedy()
  # a_star()

if __name__ == '__main__':
  main()
