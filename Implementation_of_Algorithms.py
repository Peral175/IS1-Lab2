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

# target = ["Sullust", "Cantanica"]
def dfs(visited,graph, node, target):
    visited = set()
    if node in target:
      print(target, "Found")
      quit()
    if node not in visited:
        print ("->", node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, target)


def ucs(graph, origin, target):
  list_of_next_node = []
  if origin == target:
    quit()
  while True:
    for neighbour in graph[origin]:
      list_of_next_node.append(neighbour[weight])
    break
    print(list_of_next_node)


ucs(star_galactica, 'Ajan Kloss', "whatever")
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

