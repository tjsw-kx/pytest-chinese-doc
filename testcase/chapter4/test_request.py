import smtplib

import pytest

smtp_server = ("mall.pyhton.org",587)

def test_163(smtp_connection_request):
    response, _ = smtp_connection_request.ehlo()
    assert response == 250

@pytest.fixture(scope='module',params=['smtp.163.com', "mail.python.org"])
def smtp_connection_params(request):
    server = request.param
    with smtplib.SMTP(server, 587, timeout=5) as smtp_connection:
        yield smtp_connection
        print(f"断开 {server}:587")
