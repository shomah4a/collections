#-*- coding:utf-8 -*-
u'''
Wrapper for Iterable-object that provide scala-collection like interface.
'''

import itertools


class Iterable(object):
    u'''
    Scala Iterator like class
    '''

    def __init__(self, it):

        self.iterable = it


    def map(self, f):

        return self.__class__(itertools.imap(f, self.iterable))


    def filter(self, pred):

        return self.__class__(itertools.ifilter(pred, self.iterable))


    def filter_not(self, pred):

        return self.__class__(itertools.ifilterfalse(pred, self.iterable))


    def flatmap(self, f):

        def it():

            for elem in self.iterable:

                for yld in f(elem):

                    yield yld

        return self.__class__(it())


    def take(self, n):

        return self.__class__(x[1] for x in itertools.takewhile(lambda x: x[0] < n,
                                                                enumerate(self.iterable)))


    def drop(self, n):

        return self.__class__(x[1] for x in itertools.dropwhile(lambda x: x[0] < n,
                                                                enumerate(self.iterable)))


    def takewhile(self, pred):

        return self.__class__(itertools.takewhile(pred, self.iterable))


    def dropwhile(self, pred):

        return self.__class__(itertools.dropwhile(pred, self.iterable))


    def count(self, pred):

        return len(self.iterable)


    def foldleft(self, op, default=None):

        if default is None:
            return reduce(op, self.iterable)
        return reduce(op, self.iterable, default)


    def flatten(self):

        def it():

            for items in self.iterable:

                for i in items:

                    yield i

        return self.__class__(it())        


    def __iter__(self):

        return iter(self.iterable)


    def to_list(self):

        return list(self)


    def foreach(self, f):

        for e in self:
            f(e)


    def exists(self, v):

        return v in self


    def zip(self, *iters):

        return self.__class__(itertools.izip(self, *iters))


    def zip_with_index(self):

        return self.__class__((v, i) for i, v in enumerate(self))



class _MapLike(dict):
    u'''
    override iterate method
    '''

    def __iter__(self):

        return self.iteritems()



class Map(Iterable):
    u'''
    Scala Map like class
    '''

    def __init__(self, *argl, **argd):

        self.dict = _MapLike(*argl, **argd)
        
        super(Map, self).__init__(self.dict)



    def __getitem__(self, key):

        return self.dict[key]


    def __setitem__(self, key, val):

        self.dict[key] = val


    def __str__(self):

        return self.dict.__str__()


    def __repr__(self):

        return self.dict.__repr__()


    def to_list(self):

        return list(self)


    def keys(self):

        return Iterable(self.dict.iterkeys())


    def values(self):

        return Iterable(self.dict.itervalues())


