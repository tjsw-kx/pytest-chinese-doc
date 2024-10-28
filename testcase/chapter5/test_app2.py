import pytest
from app import get
from urllib import request
from test_app import MockResponse

@pytest.fixture
def mock_response(monkeypatch):
    def mock_urlopen(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(request, 'urlopen', mock_urlopen)
    
def test_get_fixturel(mock_response):
    data = get('https://luizyao.com')
    assert data == 'luizyao.com'
    
def test_get_fixture2(mock_response):
    data = get('https://github.com')
    assert data == 'github.com'
