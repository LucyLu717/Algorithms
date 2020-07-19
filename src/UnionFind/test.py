import pytest
import UFapi
import reader


def test_quickfind():
    qf = UFapi.QuickFind(10)
    nums = reader.read("test.txt")
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 8 8 1 1 1 8 8
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 8


def test_quickunion():
    qf = UFapi.QuickUnion(10)
    nums = reader.read("test.txt")
    for p, q in nums:
        qf.union(p, q)
    # 1 1 1 8 8 1 1 1 8 8
    assert qf.connected(0, 1)
    assert qf.connected(4, 9)
    assert qf.find(6) == 1
    assert qf.find(2) == 1
    assert qf.find(8) == 8
