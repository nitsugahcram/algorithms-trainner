"""  You're given a list of edges representing an unweighted, directed
  graph with at least one node. Write a function that returns a boolean
  representing whether the given graph contains a cycle.
  For the purpose of this question, a cycle is defined as any number of
  vertices, including just one vertex, that are connected in a closed chain. A
  cycle can also be defined as a chain of at least one vertex in which the first
  vertex is the same as the last.
  The given list is what's called an adjacency list, and it represents a graph.
  The number of vertices in the graph is equal to the length of
  edges, where each index i in
  edges contains vertex i's outbound edges, in no
  particular order. Each individual edge is represented by a positive integer
  that denotes an index (a destination vertex) in the list that this vertex is
  connected to. Note that these edges are directed, meaning that you can only
  travel from a particular vertex to its destination, not the other way around
  (unless the destination vertex itself has an outbound edge to the original
  vertex).
  Also note that this graph may contain self-loops. A self-loop is an edge that
  has the same destination and origin; in other words, it's an edge that
  connects a vertex to itself. For the purpose of this question, a self-loop is
  considered a cycle.
  For a more detailed explanation, please refer to the Conceptual Overview
  section of this question's video explanation.
  """


# TIME: O(V+e), SPACE: O(V)
def deepFirstSearch(nodeId, edges, colors):
    cycleDetected = False
    if colors[nodeId] == 0:
        colors[nodeId] = 1
        for node in edges[nodeId]:
            if colors[node] == 1:
                cycleDetected = True
                break
            elif colors[node] == 2:
                cycleDetected = False
            else:
                cycleDetected = deepFirstSearch(node, edges, colors)
            if cycleDetected:
                break
        if not cycleDetected:
            colors[nodeId] = 2
    return cycleDetected


def cycleInGraph(edges):
    # Write your code here.
    colors = [0 for i in range(len(edges))]
    for node in range(len(edges)):
        if deepFirstSearch(node, edges, colors):
            return True
    return False


def test2():
    edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
    assert cycleInGraph(edges)


def test1():
    edges = [[], [0, 3], [0], [1, 2]]
    assert cycleInGraph(edges)


if __name__ == "__main__":
    test1()
    test2()