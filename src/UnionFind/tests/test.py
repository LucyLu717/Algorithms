import pytest
import os, sys

sys.path.append(os.path.dirname("./"))
sys.path.append(os.path.dirname("../utils"))

import UFapi
from utils import reader

PATH = "tests/test.txt"


def test_quickfind():
    qf = UFapi.QuickFind(10)
    nums = reader.read(PATH)
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 8 8 1 1 1 8 8
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 8
    assert qf.count() == 2


def test_quickunion():
    qf = UFapi.QuickUnion(10)
    nums = reader.read(PATH)
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 8 8 1 1 1 8 8
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 8
    assert qf.count() == 2


def test_weightedquickunion():
    qf = UFapi.WeightedQuickUnion(10)
    nums = reader.read(PATH)
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 3 3 1 1 1 3 3
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 3
    assert qf.count() == 2


def test_quickunion_compression():
    qf = UFapi.QuickUnion(10, True)
    nums = reader.read(PATH)
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 8 8 1 1 1 8 8
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 8
    assert qf.count() == 2


def test_weightedquickunion_compression():
    qf = UFapi.WeightedQuickUnion(10, True)
    nums = reader.read(PATH)
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 3 3 1 1 1 3 3
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 3
    assert qf.count() == 2


def test_weightedquickunion_height():
    qf = UFapi.WeightedQuickUnion(10, True, True)
    nums = reader.read(PATH)
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 3 3 1 1 1 3 3
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 3
    assert qf.count() == 2
    assert qf.get_height(3) == 1
    assert qf.get_height(1) == 2
    assert qf.get_height(2) == 2
