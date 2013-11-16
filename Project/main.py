import GraphGenerator as gg
import SegmentTree as st
import pdb
import random

# G = gg.Graph()
# set1 = G.create_nodes(100)
# set2 = G.create_nodes(80)
# G.create_random_edges(500, [set1, set2], [[0.49,0.02],[0.,0.49]], [gg.UniformDistrib(), gg.UniformDistrib()])
# G.plot()

# G = gg.Graph(True)
# set1 = G.create_nodes(100)
# set2 = G.create_nodes(80)
# G.create_random_edges(500, [set1, set2], [[0.49,0.01],[0.01,0.49]], [gg.UniformDistrib(), gg.UniformDistrib()])
# G.plot()





tree = st.SegmentTree()
elements = [(0,5),(0,5),(0,10),(0,7),(5,10),(15,20),(12,st.SegmentTree.infinite)]

for i in range(len(elements)):
	tree.insert(i, elements[i])

# query = [0,3,5,7,11,12,20,98]
# for q in query:
# 	print "query=",q," - result=",tree.query(q)
# 	pdb.set_trace()

to_delete = range(len(elements))
random.shuffle(to_delete)
print to_delete
for d in to_delete:
	tree.delete(d, elements[d])
	print "query=",elements[d][1]," - result=",tree.query(elements[d][1])
	pdb.set_trace()