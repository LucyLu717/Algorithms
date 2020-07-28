def read(path):
    edges = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split(" ")
            edges.append((int(nums[0]), int(nums[1])))
    return edges
