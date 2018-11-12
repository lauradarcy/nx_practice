import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def create_fig(titleString, inputGraph):
	plt.figure()
	fig = plt.gcf()
	fig.canvas.set_window_title(titleString)
	nx.draw(inputGraph, with_labels=True, font_weight='bold')

def create_subplots(titleString, subplotTitleList, graphList):
	#plt.figure()
	nr = int(np.ceil(np.sqrt(len(subplotTitleList))))
	fig, subplots = plt.subplots(nr, nr)
	fig.canvas.set_window_title(titleString)
	for i, title in enumerate(subplotTitleList):
		ix = np.unravel_index(i, subplots.shape)
		plt.sca(subplots[ix])
		nx.draw(graphList[i], with_labels=True)
		subplots[ix].set_title(title)

petersen = nx.petersen_graph()
tutte = nx.tutte_graph()
maze = nx.sedgewick_maze_graph()
tet = nx.tetrahedral_graph()

graphs = [petersen, tutte, maze, tet]
graphtitles = ['petersen', 'tutte', 'maze', 'tet']
create_subplots('types of standard graphs', graphtitles, graphs)

K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)

create_subplots('constructive generator', ['K_5', 'K_3_5', 'barbell', 'lollipop'], [K_5, K_3_5, barbell, lollipop])

plt.show()