try:
    from optparse import OptionParser
    import sys
    import networkx as nx
    import random
except ImportError as msg:
    print("[!] Library not installed: " + str(msg))
    exit()


class Trusses:

    def __init__(self):

        # Input variables
        try:
            size = int(input("Please insert the size of the trusses. "))
        except ValueError:
            print("Value Error!")
            exit(1)
        try:
            nodes = int(input("Please insert the number of nodes. "))
        except ValueError:
            print("Value Error!")
            exit(1)
        try:
            possibility = float(input("Please insert the possibility of edges. "))
        except ValueError:
            print("Value Error!")
            exit(1)

        # Create Graph
        G = nx.fast_gnp_random_graph(nodes,possibility)
        edges = nx.edges(G)

        # Remove edges that do not fit due to the size of the trusses
        boolean=True
        while boolean:
            boolean=False
            for e in edges:
                (node1, node2) = e
                if (len(self.intersect(nx.all_neighbors(G, node1), nx.all_neighbors(G, node2)))) < size - 2:
                    edges.remove(e)
                    boolean = True
        adjacency = {}

        # Create a dictionary of edges' trusses
        for e in edges:
            (node1, node2) = e
            if node1 not in adjacency.keys():
                adjacency[node1]=[node2]
            else:
                adjacency[node1].append(node2)
            if node2 not in adjacency.keys():
                adjacency[node2]=[node1]
            else:
                adjacency[node2].append(node1)

        # Print all trusses
        result=[]
        for key in adjacency:
            row=[]
            row.append(key)
            row.extend(adjacency[key])
            row.sort()
            result.append(row)
        result.sort()
        for r in result:
            print (r)

    # Find the intesection between two lists
    def intersect(self, a, b):
        intersection = list(set(a) & set(b))
        return intersection

# Execute Maze_Creation
Trusses()