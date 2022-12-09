
class ShortestPath:
    """
    This class will give the shortest path given the graph and the set of nodes.
    """

    def __init__(self, graph):
        """
        This constructor takes the graph in the form of adjacency matrix and the list of nodes as input.

        :param graph: Graph represented as an Adjacency list
        """
        self.graph = graph
        pass

    def dijkstra(self, initial, end):

        # shortest paths is a dict of nodes whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "You can't reach " + end

            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in the shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    def get_shortest_path(self, source, destination):
        """
        This function gives the shortest path in the graph for the given source and destination.

        :param source: Starting Node in the path
        :param destination: Starting Node in the path
        :return: List of nodes covered for the shortest path.
        """

        path = self.dijkstra(source, destination)
        print("The Shortest Path by your preference is", end=" ")
        for node in path:
            print(node, end="-> ")
        pass
