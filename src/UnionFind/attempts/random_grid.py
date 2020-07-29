import random
import argparse


class Connection:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def get_connection(self):
        return f"{self.p} {self.q}"


class RandomBag:
    def __init__(self):
        self.size_ = 0
        self.set_ = []

    def is_empty(self):
        return self.size_ == 0

    def size(self):
        return self.size_

    def add(self, p, q):
        self.set_.append(Connection(p, q))

    def get_random_bag(self, random_instance=None):
        if random_instance:
            random.random_instance.shuttle(self.set_)
        else:
            random.shuffle(self.set_)
        return self.set_


def generate(N, seed):
    random_instance = None
    if seed != -1:
        random_instance = random.Random(seed)
        random.seed(seed)
    bag = RandomBag()
    for i in range(N):
        for j in range(i + 1):
            if random.uniform(0, 1) <= 0.5:
                bag.add(i, j)
            else:
                bag.add(j, i)
    random_bag = bag.get_random_bag()
    assert len(random_bag) == N * (N + 1) / 2
    return random_bag


def print_bag(random_bag):
    for c in random_bag:
        print(f"{c.get_connection()}")


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
generate(args.size, args.seed)
