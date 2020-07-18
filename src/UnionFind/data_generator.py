import random
import argparse

parser = argparse.ArgumentParser(description="Parser for UF data generator")
parser.add_argument("-p", "--path", type=str, required=True, help="path to write data")
parser.add_argument("-n", "--nodes", type=int, required=True, help="size of nodes")
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

args = parser.parse_args()

random.seed(args.seed)

with open(args.path, "w") as f:
    for i in range(args.edges):
        p = random.randint(0, args.nodes - 1)
        q = random.randint(0, args.nodes - 1)
        f.write(f"{p} {q}\n")

