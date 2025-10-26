"""
    Praktikum 5

    1. Pendekatan O(n)

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

tinggi = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Pendekatan O(n)

#get index and put into dictionary
dict = []
x = 1
for t in tinggi:
    dict.append({"panjang":t, "index":x})
    x += 1
# print(f"tinggi = {tinggi}")

# bagi dua sisi L dan R
tinggi_kiri = dict[0:len(dict)//2]
tinggi_kanan = dict[len(dict):(len(dict)//2)-1:-1]
# print(f"tinggi_kiri = {tinggi_kiri}")
# print(f"tinggi_kanan = {tinggi_kanan}")

# cari panjang yang tertinggi di kiri = max_l
max_l = tinggi_kiri[0]
for l in tinggi_kiri:
    if l["panjang"] > max_l["panjang"]:
        max_l = l
# print(f"max_l = {max_l}")

# cari panjang yang tertinggi di kanan (max_r) dan kurang dari max_l dan hitung luas area dengan membandingkan tiap panjangnya.
max_area = 0
max_r = tinggi_kanan[0]
max_x = 0
for r in tinggi_kanan:
    # print(r)
    # proses hanya yang tingginya kurang dari max_l
    if(r["panjang"]<=max_l["panjang"]):
        x = r["index"] - max_l["index"]
        # print(f"x = {r["index"]} - {max_l["index"]} = {x}")
        area = x * r["panjang"]
        # print(f"max_area = {x} x {r["panjang"]} = {area}")
        if area > max_area:
            max_area = area
            max_r = r
            max_x = x

# print(f"max_l = {max_l}")
# print(f"max_r = {max_r}")
# print(f"max_x = {max_x}")
# print(f"max_area = max_r['panjang'] x max_x = {max_r["panjang"]} x {max_x}")
print(f"max_area = {max_area}\n")


"""
    Praktikum 5

    2. Graph, DFS & BFS

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

class Node(object):
    # name are string
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

class Edge(object):
    # src and dest are node
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + ' -> ' + self.dest.getName()

class Digraph(object):
    # Edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.edges = {}

    def addNode(self, node):    
        if node in self.edges:
            raise ValueError('Duplicate node')  
        else:
            self.edges[node] = []   # Nodes are represented as keys in dict

    def addEdge(self, edge):    
        src = edge.getSource()
        dest = edge.getDestination()

        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        
        self.edges[src].append(dest)    # Edges are represented by destionations as values in list associated with source key
        
    # mengembalikan daftar node
    def childrenOf(self, node): 
        return self.edges[node]
    
    # sebuah graph memiliki node apa tidak
    def hasNode(self, node):
        return node in self.edges
    
    # return node -> pencarian di adjacency list
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        
        raise NameError(name)
    
    # menampilkan graph
    def __str__(self):
        result = ''

        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' => ' + dest.getName() + '\n'

        return result[:-1] #omit final new line
    

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph():
    g = Digraph()

    cities = ["Boston", "Providence", "New York", "Chicago", "Denver", "Phoenix", "Los Angeles"]
    for name in cities:
        g.addNode(Node(name))

    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))

    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))

    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))

    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))

    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g

def printPath(path):
    if not path:
        return ''
    if len(path) == 1:
        return path[0].getName()
    return path[0].getName() + ' -> ' + printPath(path[1:])

def DFS(graph, start, end, path, shortest, toPrint = False):
    path = path + [start]
    
    if toPrint:
        print('Current DFS path:', printPath(path))
    
    if start == end:
        return path
    
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)

    return shortest

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]

    while len(pathQueue) !=0:
        # Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        
        lastNode = tmpPath[-1]
        
        if lastNode == end:
            return tmpPath
        
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)

    return None

def shortestPath(graph, start, end, toPrint = False):
    return DFS(graph, start, end, [], None, toPrint)

def testSPDFS(g, source, destination):
    # g = buildCityGraph()
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print("Shortest path from", source, "to", destination, "is", printPath(sp))
    else:
        print("There is no path from", source, "to", destination)

def testSPBFS(g, source, destination):
    # g = buildCityGraph()
    sp = BFS(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print("Shortest path from", source, "to", destination, "is", printPath(sp))
    else:
        print("There is no path from", source, "to", destination)

# print(buildCityGraph())
graph = buildCityGraph()
testSPDFS(graph, "Boston", "Phoenix")

print()

testSPBFS(graph, "Boston", "Phoenix")