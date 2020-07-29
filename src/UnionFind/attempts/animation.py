import matplotlib.pyplot as plt
from random_grid import generate
import argparse
from itertools import product

parser = argparse.ArgumentParser(description="Parser for random grid generator")
parser.add_argument("-n", "-N", "--size", type=int, required=True, help="size of grid")
parser.add_argument(
    "-s",
    "--seed",
    type=int,
    default=-1,
    help="seed for random number generator; default = 0",
)
args = parser.parse_args()
bag = generate(args.size, args.seed)
x = [i for i in range(1, args.size + 1)]
x_pos = []
y_pos = []
for p, q in product(*[x, x]):
    x_pos.append(p)
    y_pos.append(q)
plt.plot(x_pos, y_pos, "ro")
# plt.plot([1, 2], [1, 2], "ro-")
plt.savefig(f"../plots/test.png")
plt.close()

