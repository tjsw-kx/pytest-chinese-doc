import pytest

@pytest.fixture(params=[('3+5',8),
                        pytest.param(('6*9',42),
                            marks=pytest.mark.xfail,
                            id='failed')])

@pytest.mark.parametrize('test_input,expected',
                         [('3+5',8),
                         pytest.param('6*9',42,marks=pytest.mark.xfail,
                            id='failed')])

def data_set(request):
    return request.param

def test_data(data_set):
    assert eval(data_set[0]) == data_set[1]

def test_data2(test_input, expected):
    assert eval(test_input) == expected
