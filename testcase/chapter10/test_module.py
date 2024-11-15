import sys
import pytest

minversion = pytest.main.skipif(sys.version_info<(3,8),reason="更新版本")

@minversion
def test_one():
    assert True
