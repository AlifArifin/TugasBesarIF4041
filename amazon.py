import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.read_edgelist('amazon0302.txt')
print("Data Belanja 2 Maret 2003")
print(nx.info(G1))

print("5 Highest Degrees of Node")
for node, degree in nx.degree(G1):
    #print(str(node)," ",str(degree))
    if (degree == 420):
        print(node, " ", degree)
    if (degree >= 400 and degree < 420):
        print(node, " ", degree)
    if (degree >= 330 and degree < 400):
        print(node, " ", degree)
    
print("Number of connected components: "+str(nx.number_connected_components(G1)))

print("")
G2 = nx.read_edgelist('amazon0312.txt')
print("Data Belanja 12 Maret 2003")
print(nx.info(G2))
print("5 Highest Degrees of Node")
for node, degree in nx.degree(G2):
    #maks = max(maks, degree)
    
    if (degree == 2747):
        print(node, " ", degree)
    if (degree >= 2000 and degree < 2747):
        print(node, " ", degree)
    if (degree >= 1282 and degree < 2000):
        print(node, " ", degree)
    
print("Number of connected components: "+str(nx.number_connected_components(G2)))

print("")
G3 = nx.read_edgelist('amazon0505.txt')
print("Data Belanja 5 Mei 2003")
print(nx.info(G3))
print("5 Highest Degrees of Node")
for node, degree in nx.degree(G3):
    maks = max(maks, degree)
    if (degree == 2760):
        print(node, " ", degree)
    if (degree >= 1000 and degree < 2760):
        print(node, " ", degree)
print("Number of connected components: "+str(nx.number_connected_components(G3)))

print("")
G4 = nx.read_edgelist('amazon0601.txt')
print("Data Belanja 1 Juni 2003")
print(nx.info(G4))
print("5 Highest Degrees of Node")
for node, degree in nx.degree(G4):
    maks = max(maks, degree)
    if (degree == 2752):
        print(node, " ", degree)
    if (degree >= 1000 and degree < 2752):
        print(node, " ", degree)
print("Number of connected components: "+str(nx.number_connected_components(G4)))