# NetworkX Practice

also practice init git repo from command line:

```bash
vlan1480:~ laura$ cd documents/phd/repos
vlan1480:repos laura$ mkdir nx_practice
vlan1480:repos laura$ cd nx_practice
vlan1480:nx_practice laura$ git init
Initialized empty Git repository in /Users/laura/Documents/phd/repos/nx_practice/.git/
vlan1480:nx_practice laura$ 
```





create figure function:

```python
def create_fig(TitleString, inputGraph):
	plt.figure()
	fig = plt.gcf()
	fig.canvas.set_window_title(TitleString)
	nx.draw(inputGraph, with_labels=True, font_weight='bold')
    
H = nx.path_graph(10)
create_fig('H = nx.path_graph(10)', H)
```



for subplots:

```python
def create_subplots(titleString, subplotTitleList, graphList):
	nr = int(np.ceil(np.sqrt(len(subplotTitleList))))
	fig, subplots = plt.subplots(nr, nr)
	fig.canvas.set_window_title(titleString)
	for i, title in enumerate(subplotTitleList):
		ix = np.unravel_index(i, subplots.shape)
		plt.sca(subplots[ix])
		nx.draw(graphList[i], with_labels=True)
		subplots[ix].set_title(title)
        
graphs = [petersen, tutte, maze, tet]
graphtitles = ['petersen', 'tutte', 'maze', 'tet']
create_subplots('types of standard graphs', graphtitles, graphs)
```

