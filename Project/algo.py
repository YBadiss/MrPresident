#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import networkx as nx
import copy
import matplotlib.pyplot as plt

import pdb

class Node:
	tr = 5
	h = 20
	d = 0
	p = 100000

	def __init__(self, id):
		self.id = id
		self.c = self.id
		self.H = [self.id]
		self.r = False
		self.rc = 0

	def add_contact(self, node_j):
		if len(self.H) >= Node.h:
			self.H.pop(0)
		self.H.append(node_j.c)

	def do_relabel(self, a, b):
		if random.random() < 1/Node.p:
			a[self.id] = self.c
			b[self.id] = self.id
			self.c = self.id
			self.rc = 0
			self.r = True
		return a,b

	def replace_contacts(self, a, b):
		self.H = [b if val == a else val for val in self.H]

	def compute_communities_weights(self):
		weights = {k:1 for k in set(self.H)}
		for k in range(len(self.H)):
			weights[self.H[k]] += max(Node.h - Node.d*(len(self.H)-k), 1)
		return zip(weights.values(),weights.keys())

	def update_relabel(self):
		if self.rc == Node.tr:
			self.r = False
			self.rc = 0
		if self.r:
			self.rc += 1

# FindCommunity(i:Self ID, j:Connected Node):
def find_community(node_i, node_j):
	global a,b
	# if |Hi | ≥ h then
	# 	Remove the oldest contact in Hi
	# end if
	# H i = H i + cj
	node_i.add_contact(node_j)

	# if ¬ri then
	# 	With probability 1/p
	# 	Let ai = ci and bi = i
	# 	Relabel ci with bi
	# 	rci = 0
	# 	ri = T rue
	# end if
	if not node_i.r:
		a,b = node_i.do_relabel(a,b)

	# if ri then
	# 	Replace all instances of ai in Hi with bi
	# end if
	if node_i.r:
		node_i.replace_contacts(a[i],b[i])

	# if rj then
	# 	Replace all instances of aj in Hi with bj
	# end if
	if node_j.r:
		node_i.replace_contacts(a[j],b[j])

	# Let Li be a list of all communities mentioned in Hi
	# Let all communities in Li have weight 1
	# for lk in Hi do [1,3,4,1,4,5,1]
	# 	Add max(h − dk, 1) to the community lk in list Li
	# end for
	weights = node_i.compute_communities_weights()

	# ci = the highest weight community in Li
	(_,node_i.c) = max(weights)
	
	# if rci = tr then
	# 	ri = F alse
	# end if
	# 
	# if ri then
	# 	rci = rci + 1
	# end if
	node_i.update_relabel()

def create_community(G, min, max):
	for i in range(min,max+1):
		j = random.randint(min,max)
		if j >= i:
			j = j + 1 if j < max else min
		G.add_edges_from([(i, j)])
	for k in range(10000):
		i = random.randint(min,max)
		j = random.randint(min,max)
		if j >= i:
			j = j + 1 if j < max else min
		G.add_edges_from([(i, j)])

def create_join(size):
	G = nx.Graph()
	print G.nodes()
	create_community(G, 1, size/2)
	print G.nodes()
	create_community(G, size/2 + 1, size)
	print G.nodes()
	return G

# Set ci = i ∀ i {Initialize each node’s community to be its ID}
# Set Hi = {i} ∀ i {Initialize each node’s history to a meeting with itself}
# Set ri = F alse ∀ i {Initialize relabeling flag to F alse for all nodes}
# Set rci = 0 ∀ i {Initialize the relabeling counter to 0 for all nodes}
# List of nodes

#random.seed(0)
# G = nx.read_gml('jazz.net')
# G = create_join(100)
G = nx.read_graphml("karate.GraphML")
E = copy.deepcopy(G.edges())
V = {n:Node(n) for n in G.nodes()}
random.shuffle(E)

a = {n:0 for n in G.nodes()}
b = {n:0 for n in G.nodes()}

for t in xrange(len(G)):
	for (n,m) in E:
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