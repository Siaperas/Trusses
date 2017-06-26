# Trusses
A k-truss in a graph is a subset of the graph such that each link of this subset is enhanced by at least k - 2 pairs of other links which form a triangle with that link. In other words, each edge of the mesh should belong to k - 2 triangles with nodes belonging to the network.

## How does the program work


## How to run
In order to run this file from the terminal we have to give the following order

```
python trusses.py
```

After the program starts, it will ask the user to insert the size of the truss, the number of the nodes of the graph and the probability that two edges will be connected. The program using networkx to create a random graph with the already given parameters. It then finds the edges that apply to k trusses and prints the results.