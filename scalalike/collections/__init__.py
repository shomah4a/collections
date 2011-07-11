#-*- coding:utf-8 -*-
u'''
scala collection like interface for python iterato.r

Iterable object:

    >>> from scalalike.collections import Iterable
    >>> it = Iterable(range(10))
    >>> it
    <scalalike.collections.collection.Iterable object at 0x9b0428c>
    >>> it.to_list()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> it.map(lambda x:x*2).to_list()
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> it.filter(lambda x:x%2 == 0).to_list()
    [0, 2, 4, 6, 8]
    >>> it.filter(lambda x:x%2 == 0).map(lambda x:x*2).to_list()
    [0, 4, 8, 12, 16]
    >>> it.flatmap(lambda x: [x, x]).to_list()
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    >>> it.take(4).to_list()
    [0, 1, 2, 3]
    >>> it.foldleft(lambda x, y: x+y)
    45


Map object:

    >>> from scalalike.collections import Iterable
    >>> mp = Map(aa=10, bb=20)
    >>> mp
    {'aa': 10, 'bb': 20}
    >>> mp.map(lambda (k, v): (k, v*2))
    {'aa': 20, 'bb': 40}
    >>> mp.filter(lambda (k, v): k == 'bb')
    {'bb': 20}
    
'''

from collection import Iterable, Map


__version__ = '0.1.0'
__author__ = 'Shoma Hosaka'
__license__ ='LGPL'
