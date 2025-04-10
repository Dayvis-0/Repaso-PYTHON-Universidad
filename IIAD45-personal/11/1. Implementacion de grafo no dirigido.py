import networkx as nx
import matplotlib.pyplot as plt
import heapq

class UndirectedGraph:
    """Representacion enlazada de un grafo no dirigido"""

    class _Node:
        __slots__ = '_element', '_adjacent'
        
        def __init__(self, element):
            self._element = element 
            self._adjacent = set()
        
    class Position:
        """Abstraccion que representa la ubicacion de un nodo"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Devuelve el elemento almacenado en esta posicion"""
            return self._node._element
        
        def __eq__(self, other):
            """Devuelve true si representa la misma posicion """
            return type(other) is type(self) and other._node is self._node
        
    def __init__(self):
        self._nodes = [] 
        self._size = 0

    def _validate(self, p):
        """Verifica si la posicion p es valida, si es asi devuelve su nodo"""
        if not isinstance(p, self.Position):
            raise TypeError("p debe ser de tipo Position")
        if p._container is not self:
            raise ValueError("p no pertenece a este grafo")
        return p._node
    
    def _make_positon(self, node):
        """Devuelve una instancia de Posicion para un nodo"""
        return self.Position(self, node)
    
    def add_node(self, element):
        """Agrega un nodo al grafo con el elemento especificado"""
        node = self._Node(element)
        self._nodes.append(node)
        self._size += 1
        
        return self._make_positon(node) 
    
    def add_edge(self, p1, p2):
        """Conecta dos nodos con un arista no dirigida """
        n1 = self._validate(p1)
        n2 = self._validate(p2)
        n1._adjacent.add(n2)
        n2._adjacent.add(n1)
        
    def adjacent(self, p):
        """Devuelve una lista de nodos adyacentes al nodo representado por p"""
        node = self._validate(p)

        return [self._make_positon(n) for n in node._adjacent]
    
    def __len__(self):
        """Devuelve la cantidad de elementos que tiene el grafo"""
        return self._size
    
    def adjacency_list(self):
        """Devuelve la lista de adyacencia completa del grafo"""
        adj_list = {}

        for node in self._nodes:
            adj_list[node._element] = [n._element for n in node._adjacent]
            
        return adj_list
    
    def depth_first_search(self, start_pos):
        """Realiza una busqueda en profundidad en el grafo"""
        visited = set()
        stack = [start_pos]
        resu = []

        while stack:
            node = stack.pop()
            node_value = node.element()

            if node_value not in visited:
                resu.append(node_value)
                visited.add(node_value)

                for neighbor in self.adjacent(node):
                    if neighbor.element() not in visited:
                        stack.append(neighbor)
    
        return ' -> '.join(str(vert) for vert in resu)
    
    def breadth_first_search(self, start_pos):
        """Realiza un recorrido en anchura en el grafo"""
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
                        
        return ' -> '.join(str(vert) for vert in resu)
    
    def get_adjacency_matrix(self):
        """Devuelve la matriz de adyacencia del grafo"""
        matrix = [[0] * self._size for _ in range(self._size)] # Primero, crear una matriz n x n con ceros

        # Mapeo de nodos a indices
        node_to_index = {node: idx for idx, node in enumerate(self._nodes)}

        # Rellenar la matriz con 1s donde hay un artista
        for node in self._nodes:
            node_idx = node_to_index[node]

            for neighbor in node._adjacent:
                neighbor_idx = node_to_index[neighbor]
                matrix[node_idx][neighbor_idx] = 1
                matrix[neighbor_idx][node_idx] = 1 # Porque es un grafo no dirigido

        return matrix
    
    def print_adjacency_matrix(self):
        """Imprime la matriz de adyyacencia con los nodos etiquetados"""
        matrix = self.get_adjacency_matrix()

        node_to_element = {idx: node._element for idx, node in enumerate(self._nodes)}

        header = "   " + "  ".join(str(node_to_element[i]) for i in range(self._size))
        print(header)

        for i in range(self._size):
            row = "  ".join(str(matrix[i][j]) for j in range(self._size))
            print(f"{node_to_element[i]}: {row}")
            
    def find_articulation_points(self):
        """Encuentra y devuelve los puntos de articulacoin del grafo"""
        time = [0] # Tiempo de desccubrimiento (envolver en llista para que sea mutable)
        visited = set()
        disc = {}
        low = {}
        parent = {}
        articulation_points = set()

        def dfs(u, u_pos):
            visited.add(u)
            disc[u] = low[u] = time[0]
            time[0] += 1
            children = 0
            
            for v_pos in self.adjacent(u_pos):
                v = v_pos.element()

                if v not in visited:
                    parent[v] = u
                    children += 1
                    dfs(v, v_pos)
                    low[u] = min(low[u], low[v])

                    if u not in parent and children > 1:
                        articulation_points.add(u)
                    if u in parent and low[v] >= disc[u]:
                        articulation_points.add(u)
                elif v != parent.get(u, None):
                    low[u] = min(low[u], disc[v])
        
        for node in self._nodes:
            u = node._element
            
            if u not in visited:
                dfs(u, self._make_positon(node))

        return articulation_points
    
    def caminos_matrix(self):
        """Devuelve la  matriz de caminos (accesibilidad) del grafo"""
        elementos = [node._element for node in self._nodes]
        index_map = {element: i for i, element in enumerate(elementos)}
        n = len(elementos)

        # Inicializar la matriz de adyacencia
        matrix = [[0] * n for _ in range(n)]
        
        for i, node in enumerate(self._nodes):
                for neighbor in node._adjacent:
                    j = index_map[neighbor._element]
                    matrix[i][j] = 1
                    
        # Algoritmo de Floyd-Warshall para caminos
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] and matrix[k][j]:
                        matrix[i][j] = 1
                        
        # Mostrar la matriz de indices
        print("   ", "  ".join(str(el) for el in elementos))
        for i, row in enumerate(matrix):
            print(f"{elementos[i]} :", "  ".join(str(cell) for cell in row))

        return matrix
    
    def dijkstra(self, start_pos):
        """aplica el algoritmo de Dijstra para encontrar el camino mas corto desde start_pos"""
        start_node = self._validate(start_pos)        
        # Inicializar las distancias a infinito, excepto el nodo de inicio
        distances = {node._element: float('inf') for node in self._nodes}
        distances[start_node._element] = 0
        
        # Usamos una cola de prioridad (min-heap) con elementos (distancia, nodo)
        heap = [(0, start_node._element)] 
        visited = set() # Para evitar porcesar el mismo nodo mas de una vez

        while heap:
            current_dist, current_element = heapq.heappop(heap)
            
            if current_element in visited:
                continue
            
            visited.add(current_element)
            # Buscar el nodo correspondiente a current_element
            current_node = next((node for node in self._nodes if node._element == current_element),None)
            if current_node is None:
                continue
            
            # Procesar los vecinos
            for neighbor in current_node._adjacent:
                neighbor_element = neighbor._element
                # Calcular la distancia al vecino
                distance = current_dist + 1 # Asumimos peso 1 para las aristas 
                # Si encontramos una ruta mas corta, actualizamos
                if distance < distances[neighbor_element]:
                    distances[neighbor._element] = distance
                    heapq.heappush(heap, (distance, neighbor_element)) # Usar el elemento del vecino

        return distances
    
    def prim(self, start_pos):
        """Aplica el algoritmo de Prim para encontrar el Arbol de Expansion Minima (MST)"""
        start_node = self._validate(start_pos)
        mst = []
        visited = set()
        min_heap = [(0, start_node._element)] # Usamos la referencia completa del nodo en lugar de su _elemento

        total_weight = 0
        
        while min_heap:
            weight, current_element = heapq.heappop(min_heap) # current_node es ahora la referencia completa

            if current_element in visited:
                continue
            
            visited.add(current_element)
            total_weight += weight
            
            if weight != 0:
                mst.append((current_element, weight)) # Guardamos el _elemen del nodo, y su peso
                
            current_node = next((node for node in self._nodes if node._element == current_element), None)
            
            if current_node is None:
                continue

            for neighbor in current_node._adjacent:
                if neighbor._element not in visited:
                    weight_to_neighbor = 1 # Asumimo que el peso de la arista es 1
                    heapq.heappush(min_heap, (weight_to_neighbor, neighbor._element))

        return mst, total_weight
    
    def kruskal(self):
        """Aplica el algoritmo de Kruskal para encontrar el Arbol de Expansion Minima (MST)"""

        #Primero, obtener todas las aristas del grafo y ordenarlas por peso
        edges = []
        for node in self._nodes:
            for neighbor in node._adjacent:
                if node._element < neighbor._element: # Evitar duplicados de aristas 
                    edges.append((1, node._element, neighbor._element)) # Peso de las aristas, en este caso 1
        
        edges.sort() # ordenar por peso (primero el peso, luego los nodos)
        # Estructura para los conjuntos disjuntos
        parent = {}
        rank = {}

        # Inicializar cada nodo como su propio representante
        for node in self._nodes:
            parent[node._element] = node._element
            rank[node._element] = 0
            
        # Funcion para encontrar el representante de un conjunto (con compresion de ruta)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Funcion para unir dos conjuntos
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                # Unir segun el rango(altura del arbol)
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
               
        # Aplicar el algoritmo de Kruskal     
        mst = [] # Arbol de expansion minima (MST)
        total_wight = 0
        
        for wight, u, v in edges:
            if find(u) != find(v): # Si u y v no estan en el mismo conjunto
                mst.append((u,v, wight)) 
                total_wight += wight
                union(u, v) # Unir los conjuntos de u y v
            
        return mst, total_wight

    """def __str__(self):
        Devuelve una representacion en cadena del grafo
        1: [2]
        2: [3, 1]
        3: [2]
        result = ""

        for node in self._nodes:
            adj = ", ".join(str(n._element) for n in node._adjacent)
            result += f"{node._element}: [{adj}]\n"

        return result"""
    
    def __str__(self):
        """Devuelve una representación visual del grafo con conexiones entre nodos"""
        if self._size == 0:
            return "Grafo vacío"
        
        # Crear un grafo de NetworkX
        G = nx.Graph()
        
        # Añadir los nodos y las aristas desde nuestro grafo personalizado
        adj_list = self.adjacency_list()
        for node, neighbors in adj_list.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        
        # Dibujar el grafo con NetworkX y Matplotlib
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000, font_size=16, font_weight='bold', edge_color='gray')
        plt.title("Representación Visual del Grafo")
        plt.show()
        
        # Retornar un mensaje informativo
        return "Grafo visualizado"
    
gr1 = UndirectedGraph()

a_1 = gr1.add_node(1)
a_2 = gr1.add_node(2)
a_3 = gr1.add_node(3)
a_4 = gr1.add_node(4)

gr1.add_edge(a_1, a_2)
gr1.add_edge(a_2, a_3)
gr1.add_edge(a_3, a_1)
gr1.add_edge(a_2, a_4)

# Forma visual del grafo
# print(gr1)

print(f'Lista de adyacencia del grafo nodirigdo | Cada elemento contienen la lista de vertices adyacentes de un vertice')
print(gr1.adjacency_list())

print(f'\nRecorrido en profundidad | Rama mas profunda y retrocede')
print(gr1.depth_first_search(a_1))

print(f'\nRecorrido en anchura | Nodos vecinos - nodos mas distantes')
print(gr1.breadth_first_search(a_1))

print(f'\nMatriz de adyacencia | Conexiones directas entre nodos')
gr1.print_adjacency_matrix()

print(f'\nMatriz de camino Floyd-Warshall | Representa si existe un camino (cualquier longitud, directo o indirecto) entre dos nodos')
gr1.caminos_matrix()

print(f'\nPuntos de circulacion | Nodos que, si se eliminan, desconectan partes del grafo \n{gr1.find_articulation_points()}')

print(f'\nAlgoritmo de Dijkstra | Nodos mas cortos desde un origen a todos los demas nodos > 0\n{gr1.dijkstra(a_1)}')

print(f'\nAlgoritmo de Prim | Encontrar el arbol de expansion minima de un grafo no dirigido y ponderado con sus nodos')
mst, total_wight = gr1.prim(a_1)
print(f'Aristas selecccionadas (nodo, peso):\n\nNodo: {a_1.element()}, Peso: 0')

for edge in mst:
    print(f"Nodo: {edge[0]}, Peso: {edge[1]}")
print(f"\nPeso total del Arbol de Expansion Minima: {total_wight}")

print(f'\nAlgoritmo de Prim | Encontrar el arbol de expansion minima de un grafo no dirigido y ponderado con sus aristas')
mst1, total_wight1 = gr1.kruskal()
for edge in mst1:
    print(f"Nodo: {edge[0]} - {edge[1]}, Peso: {edge[2]}")
print(f"\nPeso total del Arbol de Expansion Minima: {total_wight1}")