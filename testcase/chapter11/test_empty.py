import pytest
import sys

def real_value():
    if sys.version_info >= (3,8):
        return [1, 2, 3]
    else:
        return []

@pytest.mark.parametrize('test_input',real_value())
def test_empty(test_input):
    assert test_input
