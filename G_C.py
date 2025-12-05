def is_safe(node, graph, color, c):
    """Check if placing color c on node is safe."""
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True


def solve_coloring(node, graph, color, K, N):
    """Backtracking function to assign colors to nodes."""
    if node == N:
        return True 

    for c in range(1, K + 1):
        if is_safe(node, graph, color, c):
            color[node] = c 
            if solve_coloring(node + 1, graph, color, K, N):
                return True
            color[node] = 0  

    return False


def graph_coloring_from_file(filename):
    """Reads graph from file and performs coloring."""
    with open(filename, "r") as file:
        N, M, K = map(int, file.readline().split())
        graph = [[] for _ in range(N)]

        for _ in range(M):
            u, v = map(int, file.readline().split())
            graph[u].append(v)
            graph[v].append(u)
    color = [0] * N
    if solve_coloring(0, graph, color, K, N):
        print(f"Coloring Possible with {K} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring Not Possible with {K} Colors")

graph_coloring_from_file("input.text")
