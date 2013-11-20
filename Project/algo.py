#!/usr/bin/env python
# -*- coding: utf-8 -*- 



# Set ci = i ∀ i {Initialize each node’s community to be its ID}
# Set Hi = {i} ∀ i {Initialize each node’s history to a meeting with itself}
# Set ri = F alse ∀ i {Initialize relabeling flag to F alse for all nodes}
# Set rci = 0 ∀ i {Initialize the relabeling counter to 0 for all nodes}
# List of nodes

#random.seed(0)
# G = nx.read_gml('jazz.net')
# G = create_join(100)
G = nx.read_gml("karate.gml")
E = copy.deepcopy(G.edges())
V = {n:Node(n) for n in G.nodes()}
random.shuffle(E)

a = {n:0 for n in G.nodes()}
b = {n:0 for n in G.nodes()}

for t in range(2):
	for (n,m) in E:
		# find_community(V[n],V[m])
		if random.random() > 0.5:
			find_community(V[n],V[m])
		else:
			find_community(V[m],V[n])

# nx.draw(G, None, labels={node.id+1:node.c for node in V})

for node in G.node.keys():
	G.node[node]['label'] = V[node].c
nx.write_gexf(G, "karate.gexf")

# pos = nx.draw(G, None, labels={node.id:node.c for node in V.values()})
# nx.draw_networkx(G)
# plt.show()

# for t in {0, 1, ..., T } do
# 	for (i, j) in Et do
# 		FindCommunity(i,j)
# 	end for
# end for