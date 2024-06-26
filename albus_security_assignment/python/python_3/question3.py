import heapq
import sys

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = self.create_graph()

    def create_graph(self):
        graph = {}
        for node in self.nodes:
            graph[node] = {}
        for edge in self.edges:
            node1, node2, value = edge
            graph[node1][node2] = value
            graph[node2][node1] = value
        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize

    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        unvisited_nodes.remove(current_min_node)

        neighbors = graph.get_outgoing_edges(current_min_node)

        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)

    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

init_graph = [
    ["Reykjavik", "Oslo", 5],
    ["Reykjavik", "London", 4],
    ["Oslo", "Berlin", 1],
    ["Oslo", "Moscow", 3],
    ["Moscow", "Belgrade", 5],
    ["Moscow", "Athens", 4],
    ["Athens", "Belgrade", 1],
    ["Rome", "Berlin", 2],
    ["Rome", "Athens", 2]
]

graph = Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph, "Reykjavik")

print_result(previous_nodes, shortest_path, "Reykjavik", "Belgrade")