#!/usr/bin/env python3

import sys
import logging

log = logging.getLogger(__name__)

from math import inf


def _node_index_map(adjlist):
    """Returns (nodes, index) where nodes are in lexicographical order."""
    nodes = adjlist.list_nodes()
    return nodes, {name: i for i, name in enumerate(nodes)}


def _get_node(adjlist, name):
    """Returns the AdjacencyList cell for `name`, or None if missing."""
    head = adjlist.head()
    while not head.is_empty():
        if name == head.name():
            return head
        if name < head.name():
            break
        head = head.tail()
    return None

def warshall(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Warshall's
    algorithm.

    Pre: adjlist is not empty.
    '''
    nodes, index = _node_index_map(adjlist)
    n = len(nodes)

    # Initialize reachability with: self reachable + direct edges reachable.
    adj = adjlist.adjacency_matrix()
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
        for j in range(n):
            if adj[i][j] != inf:
                reach[i][j] = True

    # Warshall: transitive closure.
    for k in range(n):
        for i in range(n):
            if not reach[i][k]:
                continue
            rik = True
            row_i = reach[i]
            row_k = reach[k]
            for j in range(n):
                if not row_i[j] and row_k[j]:
                    row_i[j] = rik and row_k[j]
    return reach

def floyd(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Floyd's algorithm.

    Pre: adjlist is not empty.
    '''
    nodes, index = _node_index_map(adjlist)
    n = len(nodes)

    # Initialize distances.
    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for (src, dst, w) in adjlist.list_edges():
        i = index[src]
        j = index[dst]
        if w < dist[i][j]:
            dist[i][j] = w

    # Floyd-Warshall for all-pairs shortest paths.
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == inf:
                continue
            for j in range(n):
                alt = dik + dist[k][j]
                if alt < dist[i][j]:
                    dist[i][j] = alt
    return dist

def dijkstra(adjlist, start_node):
    '''
    Returns the result of running Dijkstra's algorithm as two N-length lists:
    1) distance d: here, d[i] contains the minimal cost to go from the node
    named `start_node` to the i:th node in the adjacency list.
    2) edges e: here, e[i] contains the node name that the i:th node's shortest
    path originated from.

    If the index i refers to the start node, set the associated values to None.

    Pre: start_node is a member of adjlist.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 2
    b|* * 2
    c|* * *

    For start node "a", the expected output would then be:

    d: [ None, 1, 2]
    e: [ None, 'a', 'a' ]
    '''
    nodes, index = _node_index_map(adjlist)
    n = len(nodes)
    start_i = index[start_node]

    dist = [inf] * n
    prev = [None] * n
    visited = [False] * n
    dist[start_i] = 0

    for _ in range(n):
        # Pick the unvisited node with the smallest tentative distance.
        u = None
        best = inf
        for i in range(n):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i
        if u is None or best == inf:
            break

        visited[u] = True
        u_name = nodes[u]
        node = _get_node(adjlist, u_name)
        if node is None:
            continue

        edge = node.edges().head()
        while not edge.is_empty():
            v_name = edge.dst()
            v = index[v_name]
            alt = dist[u] + edge.weight()
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u_name
            edge = edge.tail()

    d = [None] * n
    e = [None] * n
    for i in range(n):
        if i == start_i:
            d[i] = None
            e[i] = None
        else:
            d[i] = dist[i]
            e[i] = prev[i]
    return d, e

def prim(adjlist, start_node):
    '''
    Returns the result of running Prim's algorithm as two N-length lists:
    1) lowcost l: here, l[i] contains the weight of the cheapest edge to connect
    the i:th node to the minimal spanning tree that started at `start_node`.
    2) closest c: here, c[i] contains the node name that the i:th node's
    cheapest edge orignated from. 

    If the index i refers to the start node, set the associated values to None.

    Pre: adjlist is setup as an undirected graph and start_node is a member.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 3
    b|1 * 1
    c|3 1 *

    For start node "a", the expected output would then be:

    l: [ None, 1, 1]
    c: [ None, 'a', 'b' ]
    '''
    nodes, index = _node_index_map(adjlist)
    n = len(nodes)
    start_i = index[start_node]

    w = adjlist.adjacency_matrix()

    in_tree = [False] * n
    lowcost = [inf] * n
    closest = [None] * n

    in_tree[start_i] = True
    lowcost[start_i] = 0

    # Initialize with edges from start_node.
    for j in range(n):
        if j == start_i:
            continue
        if w[start_i][j] != inf:
            lowcost[j] = w[start_i][j]
            closest[j] = start_node

    for _ in range(n - 1):
        # Pick next node with minimal lowcost not already in tree.
        v = None
        best = inf
        for i in range(n):
            if not in_tree[i] and lowcost[i] < best:
                best = lowcost[i]
                v = i
        if v is None:
            break
        in_tree[v] = True

        # Update costs using node v.
        for j in range(n):
            if in_tree[j] or j == v:
                continue
            if w[v][j] < lowcost[j]:
                lowcost[j] = w[v][j]
                closest[j] = nodes[v]

    l = [None] * n
    c = [None] * n
    for i in range(n):
        if i == start_i:
            l[i] = None
            c[i] = None
        else:
            l[i] = lowcost[i]
            c[i] = closest[i]
    return l, c

if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
