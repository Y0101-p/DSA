class Vertex():
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def connect(self, other, weight):
        self.neighbors[other] = weight


class Graph():
    def __init__(self,n):
        self.vertices = {}
        for i in range(n):
            self.addVertex(i)
    def addVertex(self, name):
        vertex = Vertex(name)
        self.vertices[name] = vertex

    def connect(self, name1, name2, weight):
        vertex1 = self.vertices[name1]
        vertex2 = self.vertices[name2]
        vertex1.connect(vertex2, weight)
        vertex2.connect(vertex1, weight)
    def build_laplace_matrix(self):
        laplace_matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]
        for i in range(len(self.vertices)):
            neighbors = self.vertices[i].neighbors
            for neighbor in neighbors:
                laplace_matrix[i][i]+=1
                laplace_matrix[i][neighbor.name]=-1
        return '\n'.join(map(lambda x:' '.join(map(str,x)),laplace_matrix))

