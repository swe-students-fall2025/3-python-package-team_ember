from excusegen import generate
from excusegen.main import EXCUSES

def test_generate_returns_valid_string():
    result = generate()
    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_returns_random_results():
    results = {generate() for _ in range(10)}
    assert len(results) > 1, "Function should return different results sometimes"

def test_generate_returns_valid_excuse():
    result = generate()
    assert result in EXCUSES, "Output should be one of the predefined excuses"
