import pandas as pd
from user_preference import UserPreference
from graph import Graph


class DataProcessor:
    """
    This class represents the data processor that takes the given input CSV file
    and creates a graph in the format of adjacency matrix.
    """

    def __init__(self, user_preference):
        """
        This constructor takes the user preference as input and initiates list of nodes and graph.

        :param user_preference: This is an instance of UserPreference
        """
        self.user_preference = user_preference
        self.edges = list()
        self.edge_weights = list()
        self.graph = list()
        pass

    def read_csv(self, path_to_csv_file, delimiter=","):
        """
        This function reads the input csv file and creates a list of nodes

        :param path_to_csv_file: File path of the input graph with list of edges and their weights.
        :param delimiter: This is the delimiter in the input CSV file.

        :return: None
        """
        data_frame = pd.read_csv(path_to_csv_file, sep=delimiter, header=0)

        for row in data_frame.values.tolist():
            source, destination = row[0], row[1]
            if self.user_preference == UserPreference.TOLL_COST_SAVER:
                self.edges.append((source, destination, int(row[2])))
            elif self.user_preference == UserPreference.TRAVEL_TIME_SAVER:
                self.edges.append((source, destination, int(row[3])))
            elif self.user_preference == UserPreference.IDEAL_WEATHER_SEEKER:
                # less friendly the route is, the more weight should be given for the edge.
                self.edges.append((source, destination, 100 - int(row[4])))
        return

    def create_graph(self):
        """
        This function creates the graph using the user.

        :return: Graph with user-preference as weights.
        """
        g = Graph()
        for edge in self.edges:
            g.add_edge(*edge)
        return g
