"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd_warshall -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
from sys import maxsize
NO_PATH =  maxsize
GRAPH = [[0,   7,  NO_PATH, 8],
[NO_PATH,  0,  5,  NO_PATH],
[NO_PATH, NO_PATH, 0,   2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

def main():


    def print_out_graph():

        for start_node in range(0,MAX_LENGTH):
            for end_node in range(0,MAX_LENGTH):
                distance = GRAPH[start_node][end_node]
                if distance == NO_PATH:
                    distance = NO_PATH_MARKER

            message = "Distance from Node %s to Node %s is %s" %\
                (start_node,end_node,distance)
            print (message)
    def recursive_floyd_warshall(outer_loop:int, middle_loop:int, inner_loop:int):

        def FW(graph):
            v = len(graph)
            dist = [row[:] for row in graph]  # Create a deep copy of the graph

            # Recursive function to compute shortest paths
            def RE(i, j, k):
                if k < 0:
                    return dist[i][j]  # Base case: no intermediate vertices
                without_k = RE(i, j, k - 1)
                with_k = (RE(i, k, k - 1) + RE(k, j, k - 1)) if (
                        RE(i, k, k - 1) != NO_PATH and RE(k, j, k - 1) != NO_PATH) else NO_PATH
                return min(with_k, without_k)

            # Update the distance matrix using the recursive function
            for k in range(v):
                for i in range(v):
                    for j in range(v):
                        dist[i][j] = RE(i, j, k)

            return dist


if __name__ == "__main__":
    main()
