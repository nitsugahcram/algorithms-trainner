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
def isNodeInCycle(nodeId, edges, visited, currentlyInStack):
    visited[nodeId] = True
    currentlyInStack[nodeId] = True
    for node in edges[nodeId]:
        if not visited[node]:
            if isNodeInCycle(node, edges, visited, currentlyInStack):
                return True
        elif currentlyInStack[node]:
            return True

    currentlyInStack[nodeId] = False
    return False


def cycleInGraph(edges):
    # Write your code here.
    numberOfNode = len(edges)
    visited = [False for _ in range(numberOfNode)]
    currentlyInStack = [False for _ in range(numberOfNode)]

    for node in range(numberOfNode):
        if visited[node]:
            continue
        if isNodeInCycle(node, edges, visited, currentlyInStack):
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