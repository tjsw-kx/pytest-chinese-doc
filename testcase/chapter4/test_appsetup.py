import pytest
class App:
    def __init__(self, smtp_connection):
        self.smtp_connection = smtp_connection
        
@pytest.fixture(scope='module')
def app(smtp_connection_params):
    return App(smtp_connection_params)

def test_smtp_connection_exists(app):
    assert app.smtp_connection
