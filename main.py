class DirectedGraph:
    
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertices):
        if vertices in self.graph_dict:
            return "El vértice ya existe"
        self.graph_dict[vertices] = []      

    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f"Vértice {v1.get_name()} no encontrado en el grafo")
        if v2 not in self.graph_dict:
            raise ValueError(f"Vértice {v2.get_name()} no encontrado en el grafo")
        self.graph_dict[v1].append(v2)

    def is_vertices(self, vertices):
        return vertices in self.graph_dict

    def get_vertices(self, vertices_name):
        for v in self.graph_dict:
            if vertices_name == v.get_name():
                return v
            print(f"Vértice {vertices_name} no encontrado en el grafo")

    def get_neighbors(self, vertices):
        return self.graph_dict[vertices]    

    def __str__(self):
        all_edges = ""
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name()+"------> "+v2.get_name()+"\n"
        return all_edges
            
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        print(start_vertex.get_name())
        visited.add(start_vertex)
        for neighbor in self.get_neighbors(start_vertex):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
                
    def bfs(self, start_vertex):
        from collections import deque
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        while queue:
            vertex = queue.popleft()
            print(vertex.get_name())
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def floyd_warshall(self):
        # Crear lista de vértices
        vertices = list(self.graph_dict.keys())
        n = len(vertices)
        # Crear matriz de distancias
        dist = {v1: {v2: float('inf') for v2 in vertices} for v1 in vertices}
        for v in vertices:
            dist[v][v] = 0
            for neighbor in self.graph_dict[v]:
                dist[v][neighbor] = 1  # Peso 1 por defecto, cámbialo si tienes pesos

        # Algoritmo Floyd-Warshall
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Mostrar resultados
        print("Matriz de distancias mínimas:")
        for i in vertices:
            for j in vertices:
                print(f"{i.get_name()} -> {j.get_name()}: {dist[i][j]}")
            print()
            
class UnDirected_Graph(DirectedGraph):  
    def add_edge(self, edge):
        DirectedGraph.add_edge(self, edge) 
        edge_back = Edge(edge.get_v2(), edge.get_v1())        
        DirectedGraph.add_edge(self, edge_back) 
       
class Edge:
    # Clase Edge para representar una arista dirigida entre dos vértices
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2     
    def __str__(self):
        return self.v1.get_name()+"------> "+self.v2.get_name()

class Vertex:
    # Clase Vertex para representar un vértice en el grafo
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name    
    
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.name == other.name

    def __hash__(self):
        return hash(self.name)
    
def build_graph(graph):
    g = graph()
    vertices = {}

    n = int(input("¿Cuántos vértices quieres agregar? "))
    for _ in range(n):
        name = input("Nombre del vértice: ")
        vert = Vertex(name)
        vertices[name] = vert
        g.add_vertex(vert)

    m = int(input("¿Cuántas aristas quieres agregar? "))
    for _ in range(m):
        v1 = input("Vértice origen: ")
        v2 = input("Vértice destino: ")
        if v1 in vertices and v2 in vertices:
            g.add_edge(Edge(vertices[v1], vertices[v2]))
        else:
            print("Uno de los vértices no existe. Intenta de nuevo.")
    return g

if __name__ == "__main__":
    g = build_graph(UnDirected_Graph) #build_graph(DirectedGraph)
    print(g)
    start = input("Vértice de inicio para recorridos: ")
    start_vertex = g.get_vertices(start)
    if start_vertex:
        print("Recorrido en profundidad")
        g.dfs(start_vertex)
        print("Recorrido en anchura")
        g.bfs(start_vertex)
        g.floyd_warshall()
    else:
        print("El vértice de inicio no existe.")

