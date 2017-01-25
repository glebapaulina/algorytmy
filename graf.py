# -*- encoding: utf8 -*-
class Graf:
    def __init__(self, directed=False):
        self.directed = directed
        self._vertices = []
        self._edges = []
        
    def is_directed(self):
        # zwraca informację czy graf jest skierowany
        return self.directed
    
    def add_vertex(self, v):
        # dodaje wierzchołek do grafu
        self._vertices.append(v)

    def vertex_count(self):
        return len(self._vertices)


    def vertices(self):
        return self._vertices
    
    def add_edge(self, u,v, value=None):
        # dodaje nową krawędź do grafu i przypisuje jej wartość value
        # upewnic sie ze u i v sa na liscie, jezeli nie blad
        if u not in self._vertices:
            raise Exception("Nie ma takiego wierzcholka")
        if v not in self._vertices:
            raise Exception("Nie ma takiego wierzcholka")
        self._edges.append((u, v, value))

    def get_edge(self, u, v):
        # zwraca krawędź pomiędzy u i v jako krotkę (u,v,value)
        for edge in self._edges:
            a, b, value = edge
            if u == a and v == b:
                return edge
            if not self.is_directed():
                if u == b and a == v:
                    return edge
        return None

    def edge_count(self):
        # zwraca liczbe krawędzi w grafie
        return len(self._edges)

    def get_edges(self):
        # zwraca krawędzie grafu jako listę krotek (u,v,value)
        return self._edges
            
    def incident_edges(self, v, outgoing=True):
        # zwraca listę krawędzi wychodzących z v (przychodzących do v)
        lista = []
        for edge in self._edges:
            a, b, value = edge
            if outgoing == True:
                if v == a:
                    lista.append(edge)
            else:
                if v == b:
                    lista.append(edge)
        return lista

    #
    # def degree(self, v, outgoing=True):
    #     # zwraca stopień wierzchołka grafu
    #     pass

e = Graf(True)
e.add_vertex(1)
e.add_vertex(2)
e.add_vertex(3)
e.add_edge(1,2)
e.add_edge(1,3)
e.add_edge(2,3)

# print(e.is_directed())
# print(e.vertex_count())
# print(e.edge_count())
# print(e.vertices())
# print(e.get_edges())
# print(e.get_edge(1,2))
print(e.incident_edges(3, False))