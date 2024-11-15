import pytest

@pytest.mark.parametrize('num',[1,2])
def test_failed(num):
    assert num == 1
    
