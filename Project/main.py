import GraphGenerator as gg
import CommunityDetection as cd
import pprint
import pdb

G = gg.Graph()
set1 = G.create_nodes_metadata([{"clustId":1} for i in range(100)])
set2 = G.create_nodes_metadata([{"clustId":2} for i in range(100)])
set3 = G.create_nodes_metadata([{"clustId":3} for i in range(50)])
set4 = G.create_nodes_metadata([{"clustId":4} for i in range(50)])
G.create_random_edges(1500, [set1, set2, set3, set4], 
							[[0.33,0.02,0   ,0   ],
							 [0   ,0.33,0   ,0   ],
							 [0   ,0   ,0.16,0   ],
							 [0   ,0   ,0   ,0.16]], [gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()])

G.create_random_edges(200, [set1, set2, set3, set4], 
						   [[0,0,0.5,0  ],
						    [0,0,0  ,0.5],
						    [0,0,0  ,0  ],
						    [0,0,0  ,0  ]], [gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib(), gg.UniformDistrib()],3)

tr_list = [0,5]
h_list = [1,10,20,50]
d_list = [0]
p_list = [100,100000000000000000000]

repeat = 10
results = []
for tr in tr_list:
	for h in h_list:
		for d in d_list:
			for p in p_list:
				temp = []
				for i in range(repeat):
					cdr = cd.CommunityDetector(G, tr, h, d, p)
					cdr.run()
					temp.append(cdr.compute_accuracy(False))
				results.append((sum(temp)/float(repeat), {"tr":tr,"h":h,"d":d,"p":p}))

sorted_results = sorted(results)[-10:]
pprint.pprint(sorted_results)

cdr = cd.CommunityDetector(G, sorted_results[-1][1]["tr"], sorted_results[-1][1]["h"], sorted_results[-1][1]["d"], sorted_results[-1][1]["p"])
cdr.run()
pprint.pprint(cdr.compute_accuracy(True))

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