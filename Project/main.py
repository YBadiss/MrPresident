import GraphGenerator as gg

# G = gg.Graph()
# G.plot()

# G.create_nodes(10)
# G.plot()

# # G.create_edges(nb_edges, list_of_lists_of_nodes, multinomial_between_lists, list_of_func_pointers)
# G.create_edges(15, [range(1,6),range(6,10)], [[0.25,0.25],[0.25,0.25]], [gg.UniformDistrib(), gg.GaussianDistrib(sigma,mu)])
# G.plot()

# # G.delete_edges(nb_edges, list_of_lists_of_nodes, multinomial_between_lists, list_of_func_pointers)
# G.delete_edges(5, [range(1,6),range(6,10)], [[0.25,0.25],[0.25,0.25]], [gg.UniformDistrib(), gg.GaussianDistrib(sigma,mu)])
# G.plot()

# G.delete_nodes(range(1,6))
# G.plot()

G = gg.Graph()
set1 = G.create_nodes(100)
set2 = G.create_nodes(80)
G.create_random_edges(500, [set1, set2], [[0.49,0.02],[0.,0.49]], [gg.UniformDistrib(), gg.UniformDistrib()])
G.plot()

G = gg.Graph(True)
set1 = G.create_nodes(100)
set2 = G.create_nodes(80)
G.create_random_edges(500, [set1, set2], [[0.49,0.01],[0.01,0.49]], [gg.UniformDistrib(), gg.UniformDistrib()])
G.plot()