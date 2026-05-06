from collections import deque


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited