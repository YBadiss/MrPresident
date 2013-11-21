import GraphGenerator as gg
import CommunityDetection as cd
from parameter_learner import *

G = gg.Graph()
set1 = G.create_nodes(200, {"clustId":1}, 0)
set2 = G.create_nodes(400, {"clustId":2}, 0)
set3 = G.create_nodes(50, {"clustId":3}, 0)
set4 = G.create_nodes(50, {"clustId":3}, 0)
G.create_random_edges(	2500,
						[set1, set2, set3, set4], 
						[[0.29,0.01,0   ,0   ],
						 [0   ,0.5 ,0   ,0   ],
						 [0   ,0   ,0.10,0   ],
						 [0   ,0   ,0   ,0.10]],
						[gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],
						0)

G.create_random_edges(	2500,
						[set1, set2, set3, set4], 
						[[0.29,0.01,0   ,0   ],
						 [0   ,0.5 ,0   ,0   ],
						 [0   ,0   ,0.10,0   ],
						 [0   ,0   ,0   ,0.10]],
						[gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],
						1)

G.create_random_edges(	400,
						[set1, set2, set3, set4], 
						[[0.1 ,0   ,0.4 ,0   ],
					     [0   ,0.1 ,0   ,0.4 ],
					     [0   ,0   ,0   ,0   ],
					     [0   ,0   ,0   ,0   ]],
					    [gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],
					    2)

G.create_random_edges(	500,
						[set1, set2, set3, set4], 
						[[0.2 ,0   ,0   ,0   ],
					     [0   ,0.2 ,0   ,0   ],
					     [0   ,0   ,0   ,0.6 ],
					     [0   ,0   ,0   ,0   ]],
					    [gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],
					    3)

G.create_random_edges(	500,
						[set1, set2, set3, set4], 
						[[0.2 ,0   ,0   ,0   ],
					     [0   ,0.2 ,0   ,0   ],
					     [0   ,0   ,0   ,0.6 ],
					     [0   ,0   ,0   ,0   ]],
					    [gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],
					    4)


# set5 = G.create_nodes(50, {"clustId":5}, 2)
# G.create_random_edges(	200,
# 						[set5], 
# 						[[1]],
# 					    [gg.UniformDistrib()],
# 					    2)
# G.create_random_edges(	200,
# 						[set5], 
# 						[[1]],
# 					    [gg.UniformDistrib()],
# 					    3)
# G.create_random_edges(	100,
# 						[set5], 
# 						[[1]],
# 					    [gg.UniformDistrib()],
# 					    4)


#learn_parameters(G)

# cdr = cd.CommunityDetector(G, sorted_results[-1][1]["tr"], sorted_results[-1][1]["h"], sorted_results[-1][1]["d"], sorted_results[-1][1]["p"])
cdr = cd.CommunityDetector(G, 10, 50, 5, 10000)
cdr.run(True, True)


# G.create_random_edges(200, [set1, set2], [[0,1],[0,0]], [gg.UniformDistrib(), gg.UniformDistrib()],4)
# G.create_random_edges(200, [set1, set2, set3, set4], [[0,0,0,0.5],[0,0,0.5,0],[0,0,0,0],[0,0,0,0]], [gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],5)
# G.create_random_edges(400, [set1, set2], [[0.49,0.02],[0.,0.49]], [gg.UniformDistrib(), gg.UniformDistrib()],10)
# G.plot_sequence()

# G = gg.Graph(True)
# set1 = G.create_nodes(100)
# set2 = G.create_nodes(80)
# G.create_random_edges(500, [set1, set2], [[0.49,0.01],[0.01,0.49]], [gg.UniformDistrib(), gg.UniformDistrib()])
# G.plot_sequence()





# tree = st.SegmentTree()
# elements = [(0,5),(0,5),(0,10),(0,7),(5,10),(15,20),(12,st.SegmentTree.infinite)]

# for i in range(len(elements)):
# 	tree.insert(i, elements[i])

# # query = [0,3,5,7,11,12,20,98]
# # for q in query:
# # 	print "query=",q," - result=",tree.query(q)
# # 	pdb.set_trace()

# to_delete = range(len(elements))
# random.shuffle(to_delete)
# print to_delete
# for d in to_delete:
# 	tree.delete(d, elements[d])
# 	print "query=",elements[d][1]," - result=",tree.query(elements[d][1])
# 	pdb.set_trace()