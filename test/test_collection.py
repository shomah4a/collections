#-*- coding:utf-8 -*-


from scalalike.collections import collection


def test_iterable():

    a = collection.Iterable(range(5))

    assert a.map(lambda x:x*2).to_list() == [0, 2, 4, 6, 8]

    assert a.filter(lambda x:x%2).to_list() == [1, 3]

    assert a.filter_not(lambda x:x%2).to_list() == [0, 2, 4]

    assert a.take(4).to_list() == range(4)

    assert a.drop(2).to_list() == range(5)[2:]

    assert a.foldleft(lambda x, y: x+y, 0) == 10

    assert a.map(lambda x: x*2).foldleft(lambda x,y: x+y, 0) == 20

    assert a.flatmap(lambda x: [x, x]).foldleft(lambda x,y: x+y, 0) == 20
