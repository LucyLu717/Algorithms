""" Exercise 1.5.17 """
import random
import argparse
import UFapi
from math import log
import os, sys

sys.path.append(os.path.dirname("./"))


def count(nodes, edges, model, seed):
    model = getUFModel(nodes, model)
    if seed != -1:
        random.seed(seed)
    for i in range(edges):
        p = random.randint(0, nodes - 1)
        q = random.randint(0, nodes - 1)
        model.union(p, q)
    return model.count()


# Exercise 1.5.21
def all_connected(nodes, model, seed):
    model = getUFModel(nodes, model)
    if seed != -1:
        random.seed(seed)
    connections = 0
    while model.count() != 1:
        p = random.randint(0, nodes - 1)
        q = random.randint(0, nodes - 1)
        model.union(p, q)
        connections += 1
    return connections


def getUFModel(N, model):
    if model == "qfind":
        return UFapi.QuickFind(N)
    elif model == "qunion":
        return UFapi.QuickUnion(N)
    elif model == "qunion-compression":
        return UFapi.QuickUnion(N, True)
    elif model == "weighted":
        return UFapi.WeightedQuickUnion(N)
    elif model == "weighted-compression":
        return UFapi.WeightedQuickUnion(N, True)
    elif model == "weighted-height":
        return UFapi.WeightedQuickUnion(N, True, True)
    else:
        raise ValueError(f"Unrecognized model {model} given")


parser = argparse.ArgumentParser(description="Parser for UF data generator")
parser.add_argument(
    "-n", "-N", "--nodes", type=int, required=True, help="size of nodes"
)
parser.add_argument(
    "-e", "--edges", type=int, required=True, help="number of connected pairs/edges"
)
parser.add_argument(
    "-s",
    "--seed",
    type=int,
    default=-1,
    help="seed for random number generator; default = 0",
)
parser.add_argument(
    "-m",
    "--model",
    type=str,
    default="weighted",
    help="Union find model; choices are qfind, qunion, qunion-compression, weighted, weighted-compression, weighted-height; default = weighted quick union",
)
args = parser.parse_args()
print(count(args.nodes, args.edges, args.model, args.seed))

# Exercise 1.5.21
diff = []
for n in range(1, args.nodes + 1):
    hypothesis = n * log(n) / 2
    connections = all_connected(n, args.model, args.seed)
    diff.append(connections - hypothesis)
print(float(sum(diff)) / max(len(diff), 1))
