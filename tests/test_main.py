from excusegen import get_excuse
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
