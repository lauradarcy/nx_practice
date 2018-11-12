import networkx as nx
import matplotlib.pyplot as plt

def create_fig(TitleString, inputGraph):
	plt.figure()
	fig = plt.gcf()
	fig.canvas.set_window_title(TitleString)
	nx.draw(inputGraph, with_labels=True, font_weight='bold')


G = nx.Graph()

#------Nodes-------

#G.add_node(1)
#create_fig('G.add_node(1)', G)

#G.add_nodes_from([2,3])
#create_fig('G.add_nodes_from([2,3])', G)

H = nx.path_graph(10)
create_fig('H = nx.path_graph(10)', H)

G.add_nodes_from(H)
create_fig('G.add_nodes_from(H)', G) #graph G contains the nodes of H as nodes of G

#G.add_node(H)
#create_fig('G.add_node(H)', G) #graph G contains H as a node

#------Edges--------

G.add_edge(1, 2)
create_fig('G.add_edge(1, 2)',G)

e = (2, 3)
G.add_edge(*e) #unpack edge tuple* 
create_fig('G.add_edge(*e)',G)

G.add_edges_from([(1, 6), (1, 7)])
create_fig('G.add_edges_from([(1, 6), (1, 7)])', G)

G.add_edges_from(H.edges)
create_fig('G.add_edges_from(H.edges)', G)

G.clear()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
create_fig('ignores repeats etc', G)
print(G.number_of_nodes(),G.number_of_edges())
print(list(G.nodes))

print(list(G.edges))

print(list(G.adj[1]))  # or list(G.neighbors(1))

print(G.degree[1]) # the number of edges incident to 1
print(G.edges([2, 'm']))
print(G.degree([2, 3]))

G.remove_node(2)
G.remove_nodes_from("spam")
create_fig('G.remove_nodes_from("spam")', G)
print(list(G.nodes))

G.remove_edge(1, 3)
create_fig('G.remove_edge(1,3)', G)

#------What to use as nodes and edges--------
'''
You might notice that nodes and edges are not specified as NetworkX objects. 
This leaves you free to use meaningful items as nodes and edges. 
The most common choices are numbers or strings, but a node can be any hashable object (except None), 
and an edge can be associated with any object x using G.add_edge(n1, n2, object=x).

As an example, n1 and n2 could be protein objects from the RCSB Protein Data Bank, 
and x could refer to an XML record of publications detailing experimental observations of their interaction.

We have found this power quite useful, but its abuse can lead to unexpected surprises unless one is familiar with Python. 
If in doubt, consider using convert_node_labels_to_integers() to obtain a more traditional graph with integer labels.


'''

plt.show()

