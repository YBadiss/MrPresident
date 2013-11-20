#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, pprint
import SegmentTree as st
import networkx as nx
from collections import defaultdict, Counter

class Node:
	tr = 0 # number of steps while communition propagation occurs
	h = 75 # number of link it remebers
	d = 2 # decay on the edges
	p = 100 # 1/proba to create its own community

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

class CommunityDetector(object):
	def __init__(self, graph, tr, h, d, p):
		Node.tr = tr
		Node.h = h
		Node.d = d
		Node.p = p

		self.graph = graph
		self.a = {}
		self.b = {}
		self.V = {}

	# FindCommunity(i:Self ID, j:Connected Node):
	def __find_community(self, node_i, node_j):
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
			self.a,self.b = node_i.do_relabel(self.a,self.b)

		# if ri then
		# 	Replace all instances of ai in Hi with bi
		# end if
		if node_i.r:
			node_i.replace_contacts(self.a[i],self.b[i])

		# if rj then
		# 	Replace all instances of aj in Hi with bj
		# end if
		if node_j.r:
			node_i.replace_contacts(self.a[j],self.b[j])

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

	def compute_accuracy(self, export_graph=True):
		clust_attr = "clustId" # moooooove

		labels_nodes = defaultdict(set)
		for node_id, node in self.V.items():
			labels_nodes[node.c].add(node_id)

		clust_nodes = defaultdict(set)
		G = self.graph.get_graph_at_time(st.SegmentTree.infinite)
		for node_id, node_attr in G.nodes(data=True):
			clust_nodes[node_attr[clust_attr]].add(node_id)
		clust_cnt = sorted([(len(v),k) for k,v in clust_nodes.items()])

		clust_jaccard = defaultdict(dict)
		for label, lblset in labels_nodes.items():
			for clustId, clustset in clust_nodes.items():
				clust_jaccard[clustId][label] = len(lblset.intersection(clustset)) / float(len(lblset.union(clustset)))

		matching = {}
		best_jaccard = {}
		for _,clustId in clust_cnt:
			best_jaccard_value,best_label = max([(v,k) for k,v in clust_jaccard[clustId].items()])
			best_jaccard[clustId] = best_jaccard_value
			matching[best_label] = clustId
			for _,i in clust_cnt:
				del clust_jaccard[i][best_label]

		if export_graph:
			pprint.pprint(matching)
			pprint.pprint(best_jaccard)
			for node in G.node.keys():
				G.node[node]['label'] = self.V[node].c
				if self.V[node].c in matching:
					G.node[node]['matching'] = self.V[node].c
					if G.node[node][clust_attr] == matching[self.V[node].c]:
						G.node[node]['correct'] = matching[self.V[node].c]
					else:
						G.node[node]['correct'] = -1
				else:
					G.node[node]['matching'] = -1
			nx.write_gexf(G, "graph.gexf")
			
		return sum([1 if self.V[node].c in matching else 0 for node in G.node.keys()]) / float(len(G.nodes()))

	def run(self):
		for diff,time in self.graph.get_all_diffs():
			for n in diff["remove_nodes_from"]:
				if n in self.a:
					del self.a[n]
				if n in self.b:
					del self.b[n]
				if n in self.V:
					del self.V[n]
			for n in diff["add_nodes_from"]:
				self.a[n] = 0
				self.b[n] = 0
				self.V[n] = Node(n)

			E = list(diff["add_edges_from"])
			random.shuffle(E)
			#print "Running for time =",time
			for (n,m) in E:
				# find_community(V[n],V[m])
				if random.random() > 0.5:
					self.__find_community(self.V[n],self.V[m])
				else:
					self.__find_community(self.V[m],self.V[n])