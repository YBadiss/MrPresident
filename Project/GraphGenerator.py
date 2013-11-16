import networkx as nx
import random
import bisect
import copy
import matplotlib.pyplot as plt

class Graph:
	@staticmethod
	def __compute_cdf(flattened_distrib):
		cdf = [flattened_distrib[0]]
		for idx in xrange(1,len(flattened_distrib)):
			cdf.append(flattened_distrib[idx] + cdf[idx-1])
		return cdf

	@staticmethod
	def __remove_element_from_distrib(flattened_distrib, element_idx):
		factor = flattened_distrib[element_idx]
		flattened_distrib[element_idx] = 0
		flattened_distrib = [val/(1-factor) for val in flattened_distrib]
		return flattened_distrib

	def __init__(self, is_directed=False):
		# create the graph with networkx
		self.__G = nx.DiGraph() if is_directed else nx.Graph()
		#self.__time_index = SegmentTree()

	def __flatten_matrix_distrib(self, cross_set_distribs):
		flattened = []
		for i in range(len(cross_set_distribs)):
			for j in range(len(cross_set_distribs)):
				if self.__G.is_directed() or (j >= i):
					flattened.append(cross_set_distribs[i][j])
				else:
					flattened.append(0)
		return flattened

	def create_nodes(self, node_count, t=0):
		return self.create_nodes_attr([{} for i in range(node_count)], t)

	def create_nodes_attr(self, nodes_attr, t=0):
		"""
			Creates nodes with the attributes contained in nodes_attr.
			Returns a list of ids of the created nodes
		"""
		assert t >= 0

		list_ids = []
		for attrs in nodes_attr:
			node_id = self.__G.number_of_nodes() + 1
			list_ids.append(node_id)
			self.__G.add_node(node_id, attrs)
			#self.__time_index.add_entry(node_id, (t,-1))
		return set(list_ids)

	def delete_nodes(self, nodes_idx, t=0):
		"""
			Delete the nodes with the ids contained in nodes_idx
		"""
		#for node_id in nodes_idx:
		#	_,(start_time,_) = self.__time_index.delete_entry(node_id)
		#	self.__time_index.add_entry(node_id, (start_time,t))
		pass

	def create_random_edges(self, edge_count, node_sets, cross_set_distribs, node_select_distribs, t=0):
		"""
			node_sets: size = n ; list of sets (can be of different sizes)
			cross_set_distribs: size = n x n ; matrix of floats summing to one
			node_select_distrib: size = n ; list of function pointers

			Create edge_count edges between nodes belonging to the sets of node_sets.
			The distribution of edges linking sets of nodes is discribed in the multinomial cross_set_distribs.
			Choosing which nodes within sets are actually linked together is decided using the function pointers ofode_select_distrib.

			Returns success code (True/False)
		"""
		# For each edge we find which sets are linked using the multinomial
		# Set1=smallest of the two sets ; Set2=largest of the two sets
		# We get a node n1 from Set1 using node_select_distrib
		# We create a new set of nodes from Set2 by removing the nodes already connected to n1 and removing n1
		# If the new set is empty, we remove n1 from Set1 and rdo the previous steps
		# Else, we chose an node n2 from the new set and create an edge between n1 and n2
		
		#TODO: assert the distributions sum to 1 etc.

		# flatten the cross_set_distribs
		flattened_distrib = self.__flatten_matrix_distrib(cross_set_distribs)
		cdf = Graph.__compute_cdf(flattened_distrib)
		assert cdf[-1] == 1, "cross_set_distribs must sum to 1"

		for edge in range(edge_count):
			edge_added = False
			while not edge_added:
				cdf_idx = bisect.bisect_left(cdf, random.random())
				if cdf_idx >= len(cdf):
					print "The graph is completely connected"
					return False
				i = cdf_idx % len(node_sets)
				j = int(cdf_idx / len(node_sets))

				if len(node_sets[i]) < len(node_sets[j]) or self.__G.is_directed():
					src_idx, dest_idx = i,j
				else:
					src_idx, dest_idx = j,i

				src_set, dest_set = copy.deepcopy(node_sets[src_idx]), copy.deepcopy(node_sets[dest_idx])
				src_distrib, dest_distrib = copy.deepcopy(node_select_distribs[src_idx]), copy.deepcopy(node_select_distribs[dest_idx])

				while len(src_set) > 0 and not edge_added:
					node_1 = src_distrib.get_item(src_set)
					except_set = set(self.__G[node_1].keys() + [node_1])
					filtered_destset = dest_set.difference(except_set)
					if len(filtered_destset) > 0:
						node_2 = dest_distrib.get_item(filtered_destset)
						self.__G.add_edge(node_1, node_2)
						edge_added = True
					else:
						# remove node_1 from src_set
						src_set.remove(node_1)

				if not edge_added:
					flattened_distrib = Graph.__remove_element_from_distrib(flattened_distrib, cdf_idx)
					cdf = Graph.__compute_cdf(flattened_distrib)

		return True
			# if set1 becomes empty, recompute the new cdf
			# we have to manage eges and the possibility that multiple edges between n1 and n2 can exist at different times
			# use GetGraphAtTime_t(t) ? 


	def delete_random_edges(self, edge_count, node_sets, cross_set_distribs, node_select_distrib, t=0):
		"""
			node_sets: size = n ; list of lists (can be of different sizes)
			cross_set_distribs: size = n x n ; matrix of floats summing to one
			node_select_distrib: size = n ; list of function pointers

			Delete edge_count edges between nodes belonging to the sets of node_sets.
			The distribution of edges linking sets of nodes is discribed in the multinomial cross_set_distribs.
			Choosing which nodes within sets are actually linked together is decided using the function pointers ofode_select_distrib.

			Returns success code (True/False)
		"""
		pass

	def plot(self, t=-1):
		nx.draw_networkx(self.__G)
		plt.show()



class Distribution:
	def __init__(self, **kwargs):
		pass
	def get_item(self, item_set):
		raise "Not Implemented: Distribution is an Interface"

class GaussianDistrib(Distribution):
	def __init__(self, sigma, mu):
		self.sigma = sigma
		self.mu = mu
	def get_item(self, item_set):
		pass

class UniformDistrib(Distribution):
	def get_item(self, item_set):
		return list(item_set)[random.randint(0,len(item_set)-1)]

class TestDistrib(Distribution):
	def get_item(self, item_set):
		return list(item_set)[0]
