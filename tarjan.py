def get_sccs(graph=None):
    """ Check for strongly connected components using Tarjan's algorithm"""
    # set up graph
    # graph = {1: [2], 2: [3], 3: [2], 4: []}
    sccs = []
    index = 0
    indices = {}
    lowlinks = {}
    onstack = set()
    stack = []

    def strong_connect(vertex):
        nonlocal index
        indices[vertex] = index
        lowlinks[vertex] = index
        index += 1
        stack.append(vertex)
        onstack.add(vertex)
        for to_vertex in graph[vertex]:
            if to_vertex not in indices:
                strong_connect(to_vertex)
                lowlinks[vertex] = min(lowlinks[vertex], lowlinks[to_vertex])
            elif to_vertex in onstack:
                lowlinks[vertex] = min(lowlinks[vertex], indices[to_vertex])
        if lowlinks[vertex] == indices[vertex]:
            current_scc = set()
            to_vertex = None
            while to_vertex != vertex:
                to_vertex = stack.pop()
                onstack.remove(to_vertex)
                current_scc.add(to_vertex)
            if current_scc:
                sccs.append(current_scc)
    for vertex in graph:
        if vertex not in indices:
            strong_connect(vertex)
    return [scc for scc in sccs if len(scc) > 1]
