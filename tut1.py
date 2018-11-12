import networkx as nx
import matplotlib.pyplot as plt

def create_fig(TitleString, inputGraph):
	plt.figure()
	fig = plt.gcf()
	fig.canvas.set_window_title(TitleString)
	nx.draw(inputGraph, with_labels=True, font_weight='bold')


G = nx.Graph()

#-------------


G.add_node(1)
create_fig('G.add_node(1)', G)

#-------------


G.add_nodes_from([2,3])
create_fig('G.add_nodes_from([2,3])', G)

#--------------


H = nx.path_graph(10)
create_fig('H = nx.path_graph(10)', H)


#---------------



G.add_nodes_from(H)
create_fig('G.add_nodes_from(H)', G)


#----------------
plt.show()