import pytest

@pytest.fixture
def max(request):
    return request.params - 1

@pytest.fixture
def min(request):
    return request.param + 1

# 默认 indirect 为 False
@pytest.mark.parametrize('min, max', [(1, 2), (3, 4)])
def test_indirect(min, max):
    assert min <= max
# min max 对应的实参重定向到同名的 fixture 中
@pytest.mark.parametrize('min,max',[(1,2),(3,4)],indirect=True)
def test_indirect_indirect(min, max):
    assert min >= max



@pytest.mark.parametrize('min, max', [(1, 2), (3, 4)], indirect=['max'])
def test_indirect_part_indirect(min, max):
    assert min == max


# 只将 max 对应的实参重定向到 fixture 中   
