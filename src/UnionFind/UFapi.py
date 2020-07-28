from abc import ABC, abstractmethod


class UF(ABC):
    def __init__(self, N):
        self.size_ = N
        self.id_ = [x for x in range(self.size_)]
        self.count_ = self.size_

    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def union(self, p, q):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count_


class QuickFind(UF):
    def __init__(self, N):
        super().__init__(N)

    def find(self, id):
        """ constant """
        return self.id_[id]

    def union(self, p, q):
        """ best case: constant, average and worst case: linear """
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        for i, id in enumerate(self.id_):
            if id == p_id:
                self.id_[i] = q_id
        self.count_ -= 1

    def union_amortized(self, p, q):
        """ Exercise 1.5.16 """
        p_id = self.find(p)
        q_id = self.find(q)
        cost = 2
        if p_id == q_id:
            return cost
        for i, id in enumerate(self.id_):
            if id == p_id:
                self.id_[i] = q_id
                cost += 1
        self.count_ -= 1
        return cost + self.size_


class QuickUnion(UF):
    def __init__(self, N, compression=False):
        super().__init__(N)
        self.compression = compression

    def find(self, id):
        """ best case: constant, average and worst case: linear """
        """ compression: log """
        while self.id_[id] != id:
            id = self.id_[id]
        return id

    def union(self, p, q):
        """ best case: constant, average and worst case: linear """
        """ compression: log """
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id != q_id:
            if self.compression:
                self.path_compression(p, q, p_id, q_id)
            self.id_[p_id] = q_id
            self.count_ -= 1
        return

    def path_compression(self, p, q, p_id, q_id):
        """ Exercise 1.5.12 """
        while self.id_[p] != p_id:
            idx = self.id_[p]
            self.id_[p] = q_id
            p = idx
        while self.id_[q] != q_id:
            idx = self.id_[q]
            self.id_[q] = q_id
            q = idx
        return

    def find_amortized(self, id):
        """ Exercise 1.5.16 """
        cost = 0
        while self.id_[id] != id:
            id = self.id_[id]
            cost += 2
        return id, cost

    def union_amortized(self, p, q):
        """ Exercise 1.5.16 """
        p_id, cost_p = self.find_amortized(p)
        q_id, cost_q = self.find_amortized(q)
        cost_comp = 0
        if p_id != q_id:
            cost_comp = 1
            if self.compression:
                cost_comp += self.path_compression_amortized(p, q, p_id, q_id)
            self.id_[p_id] = q_id
            self.count_ -= 1
        return cost_p + cost_q + cost_comp

    def path_compression_amortized(self, p, q, p_id, q_id):
        """ Exercise 1.5.16 """
        cost_p = 0
        while self.id_[p] != p_id:
            idx = self.id_[p]
            self.id_[p] = q_id
            p = idx
            cost_p += 3
        cost_q = 0
        while self.id_[q] != q_id:
            idx = self.id_[q]
            self.id_[q] = q_id
            q = idx
            cost_q += 3
        return cost_p + cost_q


class WeightedQuickUnion(UF):
    def __init__(self, N, compression=False, height=False):
        super().__init__(N)
        self.sz = [1] * self.size_
        self.hi = [0] * self.size_
        self.compression = compression
        self.height = height

    def find(self, id):
        """ log N """
        while self.id_[id] != id:
            id = self.id_[id]
        return id

    def find_amortized(self, id):
        """ Exercise 1.5.16 """
        cost = 0
        while self.id_[id] != id:
            id = self.id_[id]
            cost += 2
        return id, cost

    def union(self, p, q):
        """ log N """
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        if self.height:
            p_hi = self.hi[p_id]
            q_hi = self.hi[q_id]
            if p_hi < q_hi:
                self.id_[p_id] = q_id
            elif p_hi > q_hi:
                self.id_[q_id] = p_id
            else:
                self.id_[p_id] = q_id
                self.hi[q_id] += 1
        else:
            p_sz = self.sz[p_id]
            q_sz = self.sz[q_id]
            if p_sz <= q_sz:
                if self.compression:
                    self.path_compression(p, q, p_id, q_id, q_id)
                self.id_[p_id] = q_id
                self.sz[q_id] += p_sz
            else:
                if self.compression:
                    self.path_compression(p, q, p_id, q_id, p_id)
                self.id_[q_id] = p_id
                self.sz[p_id] += q_sz
        self.count_ -= 1
        return

    def union_amortized(self, p, q):
        """ Exercise 1.5.16 """
        p_id, cost_p = self.find_amortized(p)
        q_id, cost_q = self.find_amortized(q)
        cost = cost_p + cost_q
        if p_id == q_id:
            return cost
        if self.height:
            p_hi = self.hi[p_id]
            q_hi = self.hi[q_id]
            if p_hi < q_hi:
                self.id_[p_id] = q_id
            elif p_hi > q_hi:
                self.id_[q_id] = p_id
            else:
                self.id_[p_id] = q_id
                self.hi[q_id] += 1
                cost += 1
            cost += 3
        else:
            p_sz = self.sz[p_id]
            q_sz = self.sz[q_id]
            if p_sz <= q_sz:
                if self.compression:
                    cost += self.path_compression_amortized(p, q, p_id, q_id, q_id)
                self.id_[p_id] = q_id
                self.sz[q_id] += p_sz
            else:
                if self.compression:
                    cost += self.path_compression_amortized(p, q, p_id, q_id, p_id)
                self.id_[q_id] = p_id
                self.sz[p_id] += q_sz
            cost += 4
        self.count_ -= 1
        return cost

    def path_compression(self, p, q, p_id, q_id, target):
        """ Exercise 1.5.13 """
        while self.id_[p] != p_id:
            idx = self.id_[p]
            self.id_[p] = target
            p = idx
        while self.id_[q] != q_id:
            idx = self.id_[q]
            self.id_[q] = target
            q = idx
        return

    def path_compression_amortized(self, p, q, p_id, q_id, target):
        """ Exercise 1.5.16 """
        cost_p = 0
        while self.id_[p] != p_id:
            idx = self.id_[p]
            self.id_[p] = target
            p = idx
            cost_p += 3
        cost_q = 0
        while self.id_[q] != q_id:
            idx = self.id_[q]
            self.id_[q] = target
            q = idx
            cost_q += 3
        return cost_p + cost_q

    def get_height(self, id):
        if self.height:
            return self.hi[self.find(id)]
        return -1
