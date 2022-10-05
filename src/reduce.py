"""Reduce and accumulate module"""

from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')


def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    """
    assert len(x) >= 2
    x = iter(x)
    result = f(next(x), next(x))
    for element in x:
        result = f(result, element)
    return result


def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    """
    result = [None] * len(x)
    x = iter(x)
    result[0] = next(x)
    i = 1
    for element in x:
        result[i] = f(element, result[i-1])
        i += 1
    return result
