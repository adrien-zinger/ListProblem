import pytest
import solution1

def test_compute():
    lines = ['00', '0.']
    nexts = solution1.compute(0, 0, 2, 2, lines)
    assert len(nexts) is 2
    assert nexts[0] == (1, 0)
    assert nexts[1] == (0, 1)
    nexts = solution1.compute(1, 0, 2, 2, lines)
    assert len(nexts) is 2
    assert nexts[0] == (-1, -1)
    assert nexts[1] == (-1, -1)
    nexts = solution1.compute(0, 1, 2, 2, lines)
    assert len(nexts) is 2
    assert nexts[0] == (-1, -1)
    assert nexts[1] == (-1, -1)

def test_basic():
    inputs = iter(['2', '2', '00', '0.'])
    # Override the Python built-in input method
    solution1.input = lambda: next(inputs)
    expect_n = [(0, 0), (1, 0), (0, 1)]
    expect_nexts = [[(1, 0), (0, 1)],[(-1, -1), (-1, -1)], [(-1, -1), (-1, -1)]]
    for i, (n, nexts) in enumerate(solution1.outputs(*solution1.read())):
        print(f"{n} {nexts}")
        assert n == expect_n[i]
        assert nexts[0] == expect_nexts[i][0]
        assert nexts[1] == expect_nexts[i][1]
        assert i < 3

def test_horizontal():
    inputs = iter(['3', '1', '000'])
    # Override the Python built-in input method
    solution1.input = lambda: next(inputs)
    expect_n = [(0, 0), (1, 0), (2, 0)]
    expect_nexts = [[(1, 0), (-1, -1)],[(2, 0), (-1, -1)], [(-1, -1), (-1, -1)]]
    for i, (n, nexts) in enumerate(solution1.outputs(*solution1.read())):
        print(f"{i} {n} {nexts}")
        assert i < 3
        assert n == expect_n[i]
        assert len(nexts) is 2
        assert nexts[0] == expect_nexts[i][0]
        assert nexts[1] == expect_nexts[i][1]

def test_diagonal():
    inputs = iter(['4', '4', '0...', '.0..', '..0.', '...0'])
    solution1.input = lambda: next(inputs)
    expect_n = [(0, 0), (1, 1), (2, 2), (3, 3)]
    for i, (n, nexts) in enumerate(solution1.outputs(*solution1.read())):
        print(f"{i} {n} {nexts}")
        assert i < 4
        assert n == expect_n[i]
        assert len(nexts) is 2
        assert nexts[0] == (-1, -1)
        assert nexts[1] == (-1, -1)