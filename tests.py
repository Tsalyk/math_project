"""
Tests for iter_tools module
"""

import iter_tools


def count_test(start: int, step: int, limit: int) -> list:
    """
    Returns a sequence from a start number
    to limit with certain step.

    >>> len(count_test(1, 1, 10**6))
    1000000
    >>> len(count_test(1, 1, 10**2))
    100
    >>> count_test(0, 10, 100)
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    >>> count_test(0, 1, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> count_test(0, 0, 0)
    [0]
    """
    num_list = []

    for num in iter_tools.count(start, step):
        if num <= limit:
            num_list.append(num)
        else:
            break
    return num_list


def cycle_test(iterable, limit: int) -> list:
    """
    Returns a sequence with limited length.

    >>> cycle_test('ABC', 9)
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
    >>> cycle_test(['A', 'B', 'C'], 9)
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
    >>> cycle_test(['A', 'B', 'C'], 3)
    ['A', 'B', 'C']
    >>> cycle_test('ITERABLE', 8)
    ['I', 'T', 'E', 'R', 'A', 'B', 'L', 'E']
    >>> cycle_test('', 1)
    []
    """
    sequence = []

    for value in iter_tools.cycle(iterable):
        if len(sequence) < limit:
            sequence.append(value)
        else:
            break
    return sequence


def repeat_test(value, repeats: int) -> list:
    """
    Returns a sequence with n-time
    repeated value.

    >>> len(repeat_test('ABC', 1000))
    1000
    >>> repeat_test('ABC', 3)
    ['ABC', 'ABC', 'ABC']
    >>> repeat_test('aBcDeHiJ', 5)
    ['aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ']
    >>> repeat_test('test', 0)
    []
    >>> repeat_test('', 1)
    ['']
    """
    return list(iter_tools.repeat(value, repeats))


def product_test(iterable, repeat: int) -> list:
    """
    Returns a list with Cartesian product of
    elements of iterable.

    >>> len(product_test([1, 2, 3], 2))
    9
    >>> product_test('AB', 2)
    [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
    >>> product_test(['A', 'B'], 2)
    [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
    >>> product_test(['A', 'B', 'C'], 2) == product_test('ABC', 2)
    True
    >>> product_test([], 2)
    []
    """
    return list(iter_tools.product(*iterable, repeat=repeat))


def permutations_test(iterable, n: int) -> list:
    """
    Returns a list with all combinations of iterable which contains n elements.
    Order is important.

    >>> permutations_test('abc', 2)

    >>> permutations_test(['a', 'b', 'c'], 2)

    >>> permutations_test([['a'], ['b']], 3)

    >>> permutations_test('abc', 1)

    >>> permutations_test(['a', 'b', 'c'], 0)
    
    """
    pass


def combinations_test(iterable, r: int) -> list:
    """
    Returns a list with all combinations of iterable
    which contain r elements.

    >>> combinations_test('abc', 2)
    [('a', 'b'), ('a', 'c'), ('b', 'c')]
    >>> combinations_test(['a', 'b', 'c'], 2)
    [('a', 'b'), ('a', 'c'), ('b', 'c')]
    >>> combinations_test(['a', 'b', 'c'], 3)
    [('a', 'b', 'c')]
    >>> combinations_test(['a', 'b', 'c'], 1)
    [('a',), ('b',), ('c',)]
    >>> combinations_test('abc', 4)
    []
    """
    return list(iter_tools.combinations(iterable, r))


def combinations_with_replacement_test(iterable, n: int) -> list:
    """
    Returns a list with all combinations of iterable which contains n elements
    where elements could be repeated.
    Order is not important.

    >>> combinations_with_replacement_test('abc', 2)
    [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
    >>> combinations_with_replacement_test(['a', 'b'], 3)
    [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'b'), ('b', 'b', 'b')]
    >>> combinations_with_replacement_test([['a'], ['b']], 3)
    [(['a'], ['a'], ['a']), (['a'], ['a'], ['b']), (['a'], ['b'], ['b']), (['b'], ['b'], ['b'])]
    >>> combinations_with_replacement_test('abc', 1)
    [('a',), ('b',), ('c',)]
    >>> combinations_with_replacement_test('abc', 0)
    []
    """
    return list(iter_tools.combinations_with_replacement(iterable, n))


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
