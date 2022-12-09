import sys

import data_processor as dp
import shortest_path_algorithm as sp
import user_preference as up


def main():

    if len(sys.argv) < 5:
        print("Please provide the network file and user preference as command line arguments.")
        exit()

    file_path = sys.argv[1]
    user_preference = sys.argv[2]
    source = sys.argv[3]
    destination = sys.argv[4]

    print(file_path, user_preference, source, destination)

    if int(user_preference) == 1:
        user_preference = up.UserPreference.TRAVEL_TIME_SAVER
    elif int(user_preference) == 2:
        user_preference = up.UserPreference.TOLL_COST_SAVER
    elif int(user_preference) == 3:
        user_preference = up.UserPreference.IDEAL_WEATHER_SEEKER

    # Read the file and create a graph
    data_proc_object = dp.DataProcessor(user_preference)
    data_proc_object.read_csv(file_path)
    graph = data_proc_object.create_graph()

    # Find the shortest path between the source and the destination.
    sp_obj = sp.ShortestPath(graph)
    print(sp_obj.get_shortest_path(source, destination))


if __name__ == '__main__':
    main()
