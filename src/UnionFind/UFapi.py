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


class WeightedQuickUnion(UF):
    def __init__(self, N, compression=False):
        super().__init__(N)
        self.sz = [1] * self.size_
        self.compression = compression

    def find(self, id):
        """ log N """
        while self.id_[id] != id:
            id = self.id_[id]
        return id

    def union(self, p, q):
        """ log N """
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
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
