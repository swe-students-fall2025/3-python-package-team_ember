
import random
import pytest
from excusegen import get_excuse, get_excuses
from excusegen.main import EXCUSES


def test_get_excuse_returns_valid_string():
    result = get_excuse()
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_excuse_returns_random_results():
    results = {get_excuse() for _ in range(10)}
    assert len(results) > 1, "Function should return different results sometimes"

def test_get_excuse_returns_valid_excuse():
    result = get_excuse()
    all_excuses = [e for sublist in EXCUSES.values() for e in sublist]
    assert result in all_excuses, "Output should be one of the predefined excuses"

#tests for getexcuses
def test_get_excuses_returns_all_when_count_is_none():
    all_general = get_excuses("general", None)
    assert isinstance(all_general, list)
    assert all_general == list(EXCUSES["general"])

def test_get_excuses_invalid_category_raises_value_error():
    with pytest.raises(ValueError):
        get_excuses("not-a-category")

def test_get_excuses_count_type_must_be_int():
    with pytest.raises(TypeError):
        get_excuses("general","foo")

def test_get_excuses_count_must_be_nonnegative():
    with pytest.raises(ValueError):
        get_excuses("general", -1)

def test_get_excuses_count_zero_returns_empty_list():
    assert get_excuses("general", 0) == []

def test_get_excuse_count_less_than_pool_size():
    cat = random.choice(list(EXCUSES.keys()))
    n = len(EXCUSES[cat]) - 1
    res = get_excuses(cat, n)
    assert len(set(res)) == n
    assert set(res).issubset(set(EXCUSES[cat]))

def test_get_excuse_count_greater_than_pool_size():
    cat = random.choice(list(EXCUSES.keys()))
    n = len(EXCUSES[cat]) + 1
    res = get_excuses(cat, n)
    assert len(res) == n
    assert set(res).issubset(set(EXCUSES[cat]))




