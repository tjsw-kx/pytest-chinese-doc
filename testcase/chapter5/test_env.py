import os
import pytest

def get_os_user():
    username = os.getenv('USERNAME')
    
    if username is None:
        raise IOError('"USER" environment variable is not set.')
    
    return username

def test_user(monkeypatch):
    monkeypatch.setenv('USERNAME', 'john_doe')
    assert get_os_user() == 'john_doe'
    
def test_raise_exception(monkeypatch):
    monkeypatch.delenv('USERNAME', raising=False)
    with pytest.raises(IOError):
        get_os_user()

# ----------------------------------------------------------------
@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv('USERNAME', 'john_doe')
    
@pytest.fixture
def mock_env_no_user(monkeypatch):
    monkeypatch.delenv('USERNAME', raising=False)

def test_upper_to_lower(mock_env_user):
    assert get_os_user().lower() == 'john_doe'
    
def test_raise_exception(mock_env_missing):
    with pytest.raises(IOError):
        get_os_user()
