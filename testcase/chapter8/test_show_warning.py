import warnings

import pytest


def api_v1():
    warnings.warn(UserWarning('请使用新版本的API。'))
    return 1

def api_v2():
    assert api_v1() == 1

@pytest.mark.filterwarnings('ignore::UserWarning')
def test_two():
    assert api_v1() == 1
