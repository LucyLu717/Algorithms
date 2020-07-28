""" Exercise 1.5.17 """
import random
import argparse
import UFapi


def count(args):
    model = getUFModel(args.nodes, args.model)
    random.seed(args.seed)
    for i in range(args.edges):
        p = random.randint(0, args.nodes - 1)
        q = random.randint(0, args.nodes - 1)
        model.union(p, q)
    return model.count()


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
    default=0,
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
print(count(args))
