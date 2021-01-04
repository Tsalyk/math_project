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


def repeat_test(value, limit: int) -> list:
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
    items = []

    while len(items) != limit:
        items.append(next(iter_tools.repeat(value)))
    return items


def product_test(*args, repeat: int) -> list:
    """
    Returns a list with Cartesian product of
    elements of iterable.

    >>> len(product_test([1, 2, 3], repeat = 2))
    9
    >>> product_test('AB', repeat = 2)
    [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
    >>> product_test(['A', 'B'], repeat = 2)
    [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
    >>> product_test(['A', 'B', 'C'], repeat = 2) == product_test('ABC', repeat = 2)
    True
    >>> product_test([], repeat = 2)
    []
    """
    return list(iter_tools.product(*args, repeat=repeat))

def permutations_test(iterable, n: int) -> list:
    """
    Returns a list with all combinations of iterable which contains n elements.
    Order is important.

    >>> permutations_test('abc', 2)
    [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b')]
    >>> permutations_test(['a', 'b', 'c'], 2)
    [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b')]
    >>> permutations_test([['a'], ['b']], 3)
    []
    >>> permutations_test('abc', 1)
    [('a',), ('b',), ('c',)]
    >>> permutations_test(['a', 'b', 'c'], 0)
    [()]
    """
    return list(iter_tools.permutations(iterable, n))


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
    [('a',), ('b',), ('c',)]
    """
    return list(iter_tools.combinations_with_replacement(iterable, n))


assert len(count_test(1, 1, 10**6)) == 1000000
assert len(count_test(1, 1, 10**2)) == 100
assert count_test(0, 10, 100) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
assert count_test(0, 1, 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert count_test(0, 0, 0) == [0]
assert cycle_test('ABC', 9) == ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
assert cycle_test(['A', 'B', 'C'], 9) == ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
assert cycle_test(['A', 'B', 'C'], 3) == ['A', 'B', 'C']
assert cycle_test('ITERABLE', 8) == ['I', 'T', 'E', 'R', 'A', 'B', 'L', 'E']
assert cycle_test('', 1) == []
assert len(repeat_test('ABC', 1000)) == 1000
assert repeat_test('ABC', 3) == ['ABC', 'ABC', 'ABC']
assert repeat_test('aBcDeHiJ', 5) == ['aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ']
assert repeat_test('test', 0) == []
assert repeat_test('', 1) == ['']
assert len(product_test([1, 2, 3], repeat = 2)) == 9
assert product_test('AB', repeat = 2) == [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
assert product_test(['A', 'B'], repeat = 2) == [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
assert (product_test(['A', 'B', 'C'], repeat = 2) == product_test('ABC', repeat = 2)) == True
assert product_test([], repeat = 2) == []
assert permutations_test('abc', 2) == [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b')]
assert permutations_test(['a', 'b', 'c'], 2) == [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b')]
assert permutations_test([['a'], ['b']], 3) == []
assert permutations_test('abc', 1) == [('a',), ('b',), ('c',)]
assert permutations_test(['a', 'b', 'c'], 0) == [()]
assert combinations_test('abc', 2) == [('a', 'b'), ('a', 'c'), ('b', 'c')]
assert combinations_test(['a', 'b', 'c'], 2) == [('a', 'b'), ('a', 'c'), ('b', 'c')]
assert combinations_test(['a', 'b', 'c'], 3) == [('a', 'b', 'c')]
assert combinations_test(['a', 'b', 'c'], 1) == [('a',), ('b',), ('c',)]
assert combinations_test('abc', 4) == []
assert combinations_with_replacement_test('abc', 2) == [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
assert combinations_with_replacement_test(['a', 'b'], 3) == [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'b'), ('b', 'b', 'b')]
assert combinations_with_replacement_test([['a'], ['b']], 3) == [(['a'], ['a'], ['a']), (['a'], ['a'], ['b']), (['a'], ['b'], ['b']), (['b'], ['b'], ['b'])]
assert combinations_with_replacement_test('abc', 1) == [('a',), ('b',), ('c',)]
assert combinations_with_replacement_test('abc', 0) == [('a',), ('b',), ('c',)]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
