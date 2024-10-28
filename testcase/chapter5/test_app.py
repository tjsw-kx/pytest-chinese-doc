from  urllib import request

import pytest

from app import get

class MockResponse:
    
    @staticmethod
    def read():
        return b'<html><body><h1>Title</h1></body></html>'  
    
def test_get(monkeypatch):
    def mock_urlopen(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(request, 'urlopen', mock_urlopen)
    html = get('https://bing.com')
    assert '<h1>Title</h1>' in html

@pytest.fixture
def no_request(monkeypatch):
    monkeypatch.delattr('urllib.request.urlopen')
    
def test_delattr(no_request):
    data = get('https://bing.com')
    assert data == 'luizyao.com'
