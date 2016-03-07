
def init_graph():

    graph = {'A': [('B',False)],
         'B': [('A',False), ('C',False), ('C',False), ('C',False), ('D',False), ('D',False)],
         'C': [('B',False), ('B',False), ('B',False), ('D',False), ('D',False), ('D',False)],
         'D': [('B',False), ('B',False), ('C',False), ('C',False), ('C',False), ('E',False)],
         'E': [('D',False)]
         }
    return graph

# recursive path walk of graph
def path_finder(start_node, end_node, graph, current_path=[]):
    if current_path == {}:
        graph = init_graph()
    current_path += start_node  # start with start node
    if start_node == end_node:  # current path complete
        return current_path     # return trivial case #`
    if start_node not in graph.keys():  # no path
        return None                     # return trivial case 2
    # for each start node walk each edge and build a path
    for i in range(len(graph[start_node])):
        current_node, visited = graph[start_node][i]
        if not visited:
            graph[start_node][i] = [current_node, True]
            temp_path = path_finder(current_node, end_node, graph, current_path)
            if temp_path:
               return temp_path


# Graph initialized:
#  { node: [(edge, visited)...], ... }


graph = init_graph()
print(path_finder('A', 'B', graph, []))

print(path_finder('A', 'C', graph, []))
