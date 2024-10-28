import pytest


@pytest.fixture(params=[0,1], ids=['spam','ham'])
def a(request):
    return request.param

def test_a(a):
    pass

def idfn(fixture_value):
    if fixture_value ==0:
        return 'zero'
    elif fixture_value == 1:
        return 'one'
    elif fixture_value == 2:
        return 'two'
    else:
        return fixture_value
    
@pytest.fixture(params=[0,1,2,3],ids=idfn)
def b(request):
    return request.param

def test_b(b):
    pass
