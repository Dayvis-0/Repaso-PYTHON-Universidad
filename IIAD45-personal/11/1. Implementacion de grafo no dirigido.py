import networkx as nx
import matplotlib.pyplot as plt

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

        header = "   " + " ".join(str(node_to_element[i]) for i in range(self._size))
        print(header)

        for i in range(self._size):
            row = " ".join(str(matrix[i][j]) for j in range(self._size))
            print(f"{node_to_element[i]}: {row}")

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

print(f'Lista de adyacencia del grafo')
print(gr1.adjacency_list())

print(f'\nRecorrido en profundidad | Rama mas profunda y retrocede')
print(gr1.depth_first_search(a_1))

print(f'\nRecorrido en anchura | Nodos vecinos - nodos mas distantes')
print(gr1.breadth_first_search(a_1))

print(f'\nMatriz de adyacencia:')
gr1.print_adjacency_matrix()