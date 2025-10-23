from collections import deque

def find_vertices_at_distance_k(adj_list, s, k):
    n = len(adj_list)
    visited = [False] * n
    distance = [-1] * n
    
    queue = deque([s])
    visited[s] = True
    distance[s] = 0
    
    while queue:
        current = queue.popleft()
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    result = set()
    for i in range(n):
        if distance[i] == k:
            result.add(i)
    
    return result

if __name__ == "__main__":
    adj_list = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [1, 3, 5],
        [2, 4]
    ]
    
    s = 0
    k = 2
    result = find_vertices_at_distance_k(adj_list, s, k)
    print(f"Вершины на расстоянии {k} от {s}: {result}")
