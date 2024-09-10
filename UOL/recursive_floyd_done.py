from sys import maxsize

NO_PATH = maxsize
GRAPH = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"


def main():
    """
    This is the calling function for the Floyd's algorithm
    """
    result_graph = FW(GRAPH)
    print_out_graph(result_graph)


def FW(GRAPH):
    v = MAX_LENGTH
    state = {}

    def RE(i, j, k):
        if (i, j, k) in state:
            return state[(i, j, k)]
        if k == -1:
            return GRAPH[i][j]

        without_k = RE(i, j, k - 1)
        with_k = RE(i, k, k - 1) + RE(k, j, k - 1)
        result = min(with_k, without_k)
        state[(i, j, k)] = result
        return result

    for k in range(v):
        for i in range(v):
            for j in range(v):
                GRAPH[i][j] = RE(i, j, k)

    return GRAPH


def print_out_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            distance = graph[i][j]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER
            message = "Distance from Node %s to Node %s is %s" % (i, j, distance)
            print(message)


if __name__ == "__main__":
    main()