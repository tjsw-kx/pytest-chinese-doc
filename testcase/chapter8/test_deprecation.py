import warnings
import pytest

def api_call_vi():
    warnings.warn('v1版本废弃，请使用v2版本',DeprecationWarning)
    return 200

def test_deprecation():
    assert pytest.deprecated_call(api_call_vi()) == 200
