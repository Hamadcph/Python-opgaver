from concurrent.futures import ProcessPoolExecutor
from webget import download
import networkx as nx
import gzip
import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot

# Exercise 1
print("Exercise 1")
filename = "facebook_combined.txt.gz"


def download_facebook_file():
    download_link = "https://snap.stanford.edu/data/facebook_combined.txt.gz"

    shouldDownload = True

    if os.path.isfile(filename):
        print("File exists")
    else:
        download(download_link, filename)


download_facebook_file()

with gzip.open(filename, "r") as f:
    print(f"Reading file")
    graph = nx.read_edgelist(f)

print()
print()


# Exercise 2
print("Exercise 2")
print(nx.info(graph))
deg_vec = np.array([graph.degree(n) for n in graph.nodes()])
max_ind_deg = deg_vec.max()
index_name = list(graph.nodes())[np.argmax(deg_vec)]
print(
    "The node {} has the most connections with {} connections".format(
        index_name, len(list(graph.neighbors(index_name)))
    )
)

print()
print()
