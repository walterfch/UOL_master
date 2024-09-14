from sys import maxsize

NO_PATH = maxsize
NO_PATH_MARKER = "No Path"

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


def print_out_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            distance = graph[i][j]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER
            message = "Distance from Node %s to Node %s is %s" % (i, j, distance)
            print(message)


if __name__ == "__main__":

    # Provided graph for testing


    GRAPH = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]


    result_graph = FW(GRAPH)
    print_out_graph(result_graph)