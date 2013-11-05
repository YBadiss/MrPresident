#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import networkx as nx
import copy
import matplotlib.pyplot as plt

class Node:
	tr = 5
	h = 5
	d = 2
	p = 1000

	@staticmethod
	def get_next_id():
		id = Node.global_id
		Node.id += 1
		return id

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
		if random.random() > 1.0/Node.p:
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

# Set ci = i ∀ i {Initialize each node’s community to be its ID}
# Set Hi = {i} ∀ i {Initialize each node’s history to a meeting with itself}
# Set ri = F alse ∀ i {Initialize relabeling flag to F alse for all nodes}
# Set rci = 0 ∀ i {Initialize the relabeling counter to 0 for all nodes}
# List of nodes

#random.seed(0)
G = nx.read_gml('karate.gml')
E = copy.deepcopy(G.edges())
V = [Node(i-1) for i in G.nodes()]
random.shuffle(E)

a = [0 for i in range(len(E))]
b = [0 for i in range(len(E))]

for t in xrange(len(G)):
	for (i,j) in E:
		if random.random() > 0.5:
			find_community(V[i-1],V[j-1])
		else:
			find_community(V[j-1],V[i-1])

nx.draw(G, None, labels={node.id+1:node.c for node in V})
plt.show()

# for t in {0, 1, ..., T } do
# 	for (i, j) in Et do
# 		FindCommunity(i,j)
# 	end for
# end for