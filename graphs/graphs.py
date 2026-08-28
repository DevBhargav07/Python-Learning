#now we try to learn the graphs in python 
#what is a graph
#how the structure will make in graphs
#and how the graphs will be useful in realworld
#and how to use the graphs 
#applications and its uses of graphs
#why and where and how it is used.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    
    def getVertices(self):
        return list(self.gdict.keys())
    def getEnds(self):
        return list(self.gdict.values())
    
    def getEges(self):
        edgelist = []
        for ntrh in self.gdict:
            for vtrth in self.gdict[ntrh]:
                if {ntrh, vtrth} not in edgelist:
                    edgelist.append({ntrh, vtrth})
        return edgelist
    def addVertx(self, vertex, connect_vertex=None):
        if vertex not in self.gdict:
            self.gdict[vertex] = [connect_vertex] if connect_vertex else []
        return self.gdict

graph = {
    "a": ["b","c"],
    "b": ["a","d"],
    "c": ["a","d"],
    "d": ["e"],
    "e": ["d","f"],
    "f": ["e"]
}

g = Graph(graph)
print(g.getVertices())
print(g.getEnds())
g.addVertx("h", "e")
print(g.getEges())
print(g.getVertices())
print(g.getEnds())
print(g.getEges())
