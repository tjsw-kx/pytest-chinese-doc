import pytest
import time

def expensive_computation():
    print("running expensive computation...")
    
@pytest.fixture
def mydata(request):
    # None 是 get 方法的第二个参数，它的作用是指定当缓存中没有找到对应的键 "example/value" 时，get 方法应该返回的默认值。
    val= request.config.cache.get("example/value",None)
    if val is None:
        expensive_computation()
        val = 42
        request.config.cache.set("example/value",val)
    return val

def test_mydata(mydata):
    assert mydata == 23
