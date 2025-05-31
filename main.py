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
    
def build_graph(graph):
    g = graph()
    vertices = {}
    for v in ("s", "a", "b", "c", "d"):
        vert = Vertex(v)
        vertices[v] = vert
        g.add_vertex(vert)
    g.add_edge(Edge(vertices["s"], vertices["a"]))
    g.add_edge(Edge(vertices["s"], vertices["b"]))
    g.add_edge(Edge(vertices["a"], vertices["c"]))
    g.add_edge(Edge(vertices["a"], vertices["d"]))
    g.add_edge(Edge(vertices["b"], vertices["c"]))
    g.add_edge(Edge(vertices["b"], vertices["d"]))
    g.add_edge(Edge(vertices["c"], vertices["d"]))
    g.add_edge(Edge(vertices["d"], vertices["s"]))
    return g

if __name__ == "__main__":
    g = build_graph(DirectedGraph)
    print(g)
    print("Recorrido en profundidad")
    g.dfs(g.get_vertices("s"))
    g.floyd_warshall()

