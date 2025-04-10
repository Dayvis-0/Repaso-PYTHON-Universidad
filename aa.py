import heapq

def dijkstra(self, start_pos):
    """aplica el algoritmo de Dijstra para encontrar el camino mas corto desde start_pos"""
    start_node = self._validate(start_pos)        
    distances = {node._element: float('inf') for node in self._nodes}
    distances[start_node._element] = 0
    
    heap = [(0, start_node._element)]
    visited = set()

    while heap:
        current_dist, current_element = heapq.heappop(heap)
        
        if current_element in visited:
            continue
        
        visited.add(current_element)
        current_node = next((node for node in self._nodes if node._element == current_element),None)
        if current_node is None:
            continue

        for neighbor in current_node._adjacent:
            neighbor_element = neighbor._element
            distance = current_dist + 1
            if distance < distances[neighbor_element]:
                distances[neighbor._element] = distance
                heapq.heappush(heap, (distance, neighbor_element))

    return distances