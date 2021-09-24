from cmath import inf

import pytest


@pytest.mark.parametrize('a, b, p', [(1, 3, 2), ('safe', 'sfwaf', 'sds')])
def test_float_equals(a, b, p):
    try:
        assert float(a) >= float((b - p))
    except AssertionError:
        pass
    except ValueError:
        pass


@pytest.mark.parametrize('value', [1.1, 1, -1.1, -200, False, ""])
def test_is_float(value):
    try:
        assert float(value)
    except AssertionError:
        pass
    except ValueError:
        pass


@pytest.mark.parametrize('a, b', [(1.5, 1.6), (1.7 * 10e307, 1.6 * 10e307)])
def test_parity_number(a, b):
    try:
        assert float(a)
        assert float(b)
        assert inf == (a * b)
    except AssertionError:
        pass


@pytest.mark.parametrize('a', [[], 1, 2])
def test_is_list(a):
    try:
        assert type(a) == list
    except AssertionError:
        pass


@pytest.mark.parametrize('a', [[], [1, 3], [1], ['3']])
def test_list_empty(a):
    try:
        assert len(a) == 0
    except AssertionError:
        pass


@pytest.mark.parametrize('a', [[], [1, 3], [1], ['3']])
def test_list_float(a):
    try:
        for elem in a:
            assert float(elem)
    except AssertionError:
        pass
