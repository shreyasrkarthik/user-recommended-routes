from collections import defaultdict


class Graph:
    """
    This class represents a graph constructed using adjacency lists.
    """
    def __init__(self):
        """
        """
        self.edges = defaultdict(list)
        self.weights = {}
        self.nodes = set()

    def add_edge(self, from_node, to_node, weight):
        """
        This function adds an edge to the graph.

        :param from_node: Start Node
        :param to_node: End Node
        :param weight: Weight of the
        """
        # Edges are bidirectional or undirected.
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def get_nodes(self):
        """
        This function returns a list of nodes that are in the graph.

        :return: List of nodes
        """
        return {k: v for v, k in enumerate(self.nodes)}

    def print_graph(self):
        pass
