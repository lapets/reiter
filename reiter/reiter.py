"""Random-access interface for iterables.

Wrapper for Python iterators and iterables that implements a list-like
random-access interface by caching retrieved items for later reuse.
"""

from __future__ import annotations
import doctest
from collections.abc import Iterator
from itertools import chain

class reiter(Iterator):
    """
    Wrapper class for iterators and iterables.
    """
    def __new__(cls, iterable):
        """
        Constructor that wraps an iterator or iterable.
        """
        if isinstance(iterable, reiter):
            return iterable

        if not isinstance(iterable, Iterator):
            try:
                iterable = iter(iterable)
            except:
                raise TypeError('supplied object is not iterable')

        instance = super().__new__(cls)
        instance._iterable = iter(iterable)
        instance._iterated = []
        instance._complete = False
        return instance

    def __next__(self):
        """
        Substitute definition that caches the retrieved
        item before returning it.
        """
        item = self._iterable.__next__()
        self._iterated.append(item)
        return item

    def __getitem__(self, index):
        """
        Returns the item at the specified index, retrieving
        additional items from the iterator (and caching them)
        as necessary to reach the specified index.
        """
        if len(self._iterated) <= index:
            for index in range(len(self._iterated), index + 1):
                try:
                    item = next(self._iterable)
                    self._iterated.append(item)
                except StopIteration:
                    self._complete = True

        if index >= len(self._iterated):
            raise IndexError('index out of range')

        return self._iterated[index]

    def __iter__(self):
        """
        Build a new iterator that begins at the first cached
        element and continues from there. This method 
        is an effective way to "reset" the iterator.
        """
        for item in self._iterated:
            yield item
        while True:
            try:  
                item = self._iterable.__next__()
                self._iterated.append(item)
                yield item
            except StopIteration:
                break

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
