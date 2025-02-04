""" Exercise 1.5.16 """
import random
import subprocess
import matplotlib.pyplot as plt

import os, sys

sys.path.append(os.path.dirname("./"))
sys.path.append(os.path.dirname("../utils"))

import UFapi
from utils import reader


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


def run(path, N, model_str):
    model = getUFModel(N, model_str)
    edges = reader.read(path)
    total_res = []
    cost_res = []
    total = 0
    for i, (p, q) in enumerate(edges):
        cost = 0
        cost = model.union_amortized(p, q)
        total += cost
        total_res.append(total / (i + 1))
        cost_res.append(cost)
    index = [i + 1 for i in range(len(edges))]
    plt.xlim(right=900)
    plt.ylim(top=1200)
    plt.scatter(index, total_res, c="red", s=0.1, label="Connections")
    plt.scatter(index, cost_res, c="gray", s=0.1, label="Accesses")
    plt.legend(loc="upper right")
    plt.title(f"{model_str} 625/900 amortized")
    plt.savefig(f"plots/{model_str}_625_900_amortized.png")
    plt.close()


subprocess.run(
    [
        "python",
        "utils/data_generator.py",
        "-p",
        "mediumUF.txt",
        "-n",
        "625",
        "-e",
        "900",
    ]
)
for model in ["qfind", "qunion", "weighted"]:
    run("mediumUF.txt", 625, model)
