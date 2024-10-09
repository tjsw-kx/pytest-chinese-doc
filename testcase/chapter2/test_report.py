import pytest

@pytest.fixture
def error_fixture():
    assert 0
    
def test_ok():
    print("ok")
    
def test_fail():
    assert 0

def test_error(error_fixture):
    pass 

def test_skip():
    pytest.skip("skipping this test")

def test_skip():
    pytest.xfail("xfailing this test")
    
def test_xfail():
    pytest.xfail("xfailing this test")
   
@pytest.mark.xfail(reason="always xfail") 
# reason 参数可以用来描述为什么这个测试是预期失败的。在这里，它被设置为 "always xfail"，意味着这个测试应该始终失败。
def test_xpass():
    pass

