import networkx as nx
import matplotlib.pyplot as plt
import heapq    

class DirectedGraph:
    """Representacion enlazada de un rafo dirigido"""

    class _Node:
        __slots__ = '_element', '_adjacent'

        def __init__(self, element):
            self._element = element
            self._adjacent = set() # Ahora solo representa aristas salientes
            
    class Position:
        """Abstraccion que representa la ubicacion de un nodo"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        
        def __hash__(self):
            """Hace la clase hashable"""
            return hash(self._node._element)
        
    def __init__(self):
        self._nodes = []
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p debe ser de tipo Position')
        if p._container is not self:
            raise ValueError('p no pertenece a este grafo')

        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node)

    def add_node(self, element):
        node = self._Node(element)
        self._nodes.append(node)
        self._size += 1
        
        return self._make_position(node) 

    def add_edge(self, p_from, p_to):
        """Agrega una arista dirigida de  p_from -> p_to"""
        n_from = self._validate(p_from)
        n_to = self._validate(p_to)

        n_from._adjacent.add(n_to)
        
    def adjacent(self, p):   
        """Devuelve los nodos adyacentes salientes al nodo representado por p"""
        node = self._validate(p)

        return [self._make_position(n) for n in node._adjacent]
        
    def __len__(self):
        return self._size
        
    def adjacency_list(self):
        """Devuelve la lista de adyacencia del grafo dirigido"""
        adj_list = {}

        for node in self._nodes:
            adj_list[node._element] = [n._element for n in node._adjacent]

        return adj_list
    
    def depth_first_search(self, start_pos):
        """Realliza un recorrido en profundidad (DFS) en el grafo digido"""
        visited = set() 
        stack = [start_pos]
        resu = []

        while stack:
            node = stack.pop()
            node_value = node.element()

            if node_value not in visited:
                resu.append(node_value)
                visited.add(node_value)

                # Agregar los vecinos del nodo a la pila, en orden inverso
                for neighbor in reversed(self.adjacent(node)):
                    if neighbor.element() not in visited:
                        stack.append(neighbor)

        return " -> ".join(str(j) for j in resu)
    
    def breadth_first_search(self, start_pos):
        """Realiza un recorrido en anchura (BFS) en el grafo dirrigido"""     
        from collections import deque
        
        visited = set()
        queue = deque([start_pos])
        resu = []

        while queue:
            node = queue.popleft()
            node_value = node.element()

            if node_value not in visited:
                resu.append(node_value)
                visited.add(node_value)

                for neighbor in self.adjacent(node):
                    if neighbor.element() not in visited:
                        queue.append(neighbor)

        return " -> ".join(str(j) for j in resu)
    
    def path_matrix(self):
        """Genera la matriz de caminos para el grafo dirigido"""
        elementos = [node._element for node in self._nodes]
        index_map = {element: i for i, element in enumerate(elementos)}
        n = len(elementos)
        
        matrix = [[0] * n for _ in range(n)]

        for i, node in enumerate(self._nodes):
            for neighbor in node._adjacent:
                j = index_map[neighbor._element]
                matrix[i][j] = 1 
                
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] and matrix[k][j]:
                        matrix[i][j] = 1
                        
        print("  ", "  ".join(str(el) for el in elementos))
        for i, row in enumerate(matrix):
            print(f"{elementos[i]}:", "  ".join(str(cell) for cell in row))
                    
        return matrix
    
    def dfs_visit(self, node, visited, discovery, low, parent, articulation_points, time):
        """DFS auxiliar para encontrar los puntos de circulacion"""
        visited[node._element] = True
        discovery[node._element] = low[node._element] = time
        time += 1
        children = 0
        
        for neighbor in self.adjacent(self._make_position(node)):
            if not visited[neighbor.element()]:
                children += 1
                parent[neighbor.element()] = node._element
                self.dfs_visit(self._validate(neighbor), visited, discovery, low, parent, articulation_points, time)
                low[node._element] = min(low[node._element], low[neighbor.element()])
                
                if (parent[node._element] is None and children > 1) or (parent[node._element] is not None and low[neighbor.element()] >= discovery[node._element]):
                    articulation_points.add(node._element)
            elif neighbor.element() != parent.get(node._element):
                low[node._element] = min(low[node._element], discovery[neighbor.element()])
    
    def find_articulation_points(self):
        """Encuentra los puntos de circulacioin en el grafo dirigido"""
        visited = {node._element: False for node in self._nodes}
        discovery = {node._element: -1 for node in self._nodes}
        low = {node._element: -1 for node in self._nodes}
        parent = {node._element: None for node in self._nodes}
        articulation_points = set()
        time = 0
        
        for node in self._nodes:
            if not visited[node._element]:
                self.dfs_visit(node, visited, discovery, low, parent, articulation_points, time)
        
        return articulation_points
                
    def topological_sort(self):
        """Realiza la ordenacion topologica del grafo dirigido"""
        visited = set()
        stack = []

        def dfs(node):
            """Funcion recursiva para DFS y agregacion al stack"""
            if node in visited:
                return 
            visited.add(node)
            for neighbor in self.adjacent(node):
                dfs(neighbor)
            stack.append(node.element())
        
        for node in self._nodes:
            dfs(self._make_position(node))
            
        return stack[::-1]
    
    def dijkstra(self, start_pos):
        """Implementa el algoritmo de Dijstra para encontrar el camino mas corto desde un nodo fuente"""
        # Inicializar la distancia a todos los nodos como infinito 
        distances = {node._element: float('inf') for node in self._nodes}
        distances[start_pos.element()] = 0 # La distancia al nodo fuente es 0
        # Inicializar el diccionario de padres para recontruir el camino mas corto
        parents = {node._element: None for node in self._nodes}
        # Usamos una cola de prioriadad para seleccionar el nodo con la distancnia mas corta
        pq = [(0, start_pos)]

        while pq:
            current_distance, current_node_pos = heapq.heappop(pq)
            current_node = current_node_pos.element()
            
            # Si la distancia actual es mayor que la ya encontrada, saltamos este nodo
            if current_distance > distances[current_node]:
                continue
            
            # Recorremos los nodos adyacentes
            for neighbor_pos in self.adjacent(current_node_pos):
                neighbor = neighbor_pos.element()
                weight = 1 # Asumimo 1, aunque puedes cambiarlo por un pero variable
                new_distance = current_distance + weight
                # Si encontramos una distancia mas corta, la actualizamos
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parents[neighbor] = current_node
                    heapq.heappush(pq, (new_distance, neighbor_pos))

        # Reconstruir el camino mas corto
        def reconstruct_path(end_pos):
            path = []
            current = end_pos.element()

            while current is not None:
                path.append(current)
                current = parents[current]

            return path[::-1]

        return distances, {node._element: reconstruct_path(self._make_position(node)) for node in self._nodes}
    

    def __str__(self):
        """Devuelve una representacion visual del grafo dirigido"""
        if self._size == 0:
            return  "Grafo vacio"

        G = nx.DiGraph() # grafo dirigido

        # Añadir nodos y aristas dirigidas
        for node in self._nodes:
            for neighbor in node._adjacent:
                G.add_edge(node._element, neighbor._element)

        plt.figure(figsize=(8,6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color = 'lightblue', node_size = 3000,
                font_size=16, font_weight='bold', edge_color='gray', arrows=True, arrowsize=20)
        plt.title("Representacio visual del grafo dirigido")
        plt.show()

        return "Grafo dirigido visualizado"
        
grd1 = DirectedGraph()

a_1 = grd1.add_node(1)
a_2 = grd1.add_node(2)
a_3 = grd1.add_node(3)

grd1.add_edge(a_1, a_2)
grd1.add_edge(a_2, a_3)

# Representacion visual del grafo dirigido
# print(grd1)
print(f"Lista ed adyacencia del grafo dirigido | Cada elemento contienen la lista de vertices adyacentes de un vertice")
print(grd1.adjacency_list())

print(f"\nRecorrido en profundidad | Rama mas profunda y retrocede")
print(grd1.depth_first_search(a_1))

print(f"\nRecorrido en anchurra | Nodos vecinos - nodos mas distantes")
print(grd1.breadth_first_search(a_1))

print(f"\nMatriz de camino | Representa si existe un camino entre dos nodos")
grd1.path_matrix()

articulation_points = grd1.find_articulation_points()
print(f"\nPuntos de articulacion | Nodos que, si se eliminan, desconectan partes del grafo")
print(articulation_points)

print("\nOrdenacion Topologica | Cada arista dirigida u -> v, el nodo u aparece antes que v")
print(grd1.topological_sort())

print(f"\nAlgoritmo de Dijkstra | Nodos mas cortos desde un origen hasta todos los demas nodos > 0")
distances, paths = grd1.dijkstra(a_1)
print(f"\nDistancias mas cortas desde el nodo 1:")
for node, distance in distances.items():
    print(f"Distancia al nodo {node}: {distance}")

print(f"\nCaminos mas cortos desde el nodo 1:")
for node, path in paths.items():
    print(f"Camino al nodo {node}: {" -> ".join(map(str, path))}")
