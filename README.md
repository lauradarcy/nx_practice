# NetworkX Practice

also practice init git repo from command line

```bash
vlan1480:~ laura$ cd documents/phd/repos
vlan1480:repos laura$ mkdir nx_practice
vlan1480:repos laura$ cd nx_practice
vlan1480:nx_practice laura$ git init
Initialized empty Git repository in /Users/laura/Documents/phd/repos/nx_practice/.git/
vlan1480:nx_practice laura$ 
```





Create figure function

```python
def create_fig(TitleString, inputGraph):
	plt.figure()
	fig = plt.gcf()
	fig.canvas.set_window_title(TitleString)
	nx.draw(inputGraph, with_labels=True, font_weight='bold')
    
H = nx.path_graph(10)
create_fig('H = nx.path_graph(10)', H)
```

