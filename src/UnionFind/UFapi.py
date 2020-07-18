from abc import ABC, abstractmethod


class UF(ABC):
    def __init__(self, N):
        self.size_ = N
        self.id_ = [x for x in range(self.size_)]

    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def union(self, p, q):
        pass

    def connected(self, p, q):
        return self.id_[p] == self.id_[q]


class QuickFind(UF):
    def __init__(self, N):
        super().__init__(N)

    def find(self, id):
        return self.id_[id]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        for i, id in enumerate(self.id_):
            if id == p_id:
                self.id_[i] = q_id
