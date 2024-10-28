import pytest

# @pytest.fixture
# def smtp_connection():
#     import smtplib
# 
#     return smtplib.SMTP("smtp.163.com", 25, timeout=5)
# 
# def test_ehlo(smtp_connection):
#     response, _ = smtp_connection.ehlo()
#     assert response == 250
#     assert 0  # 为了展示，强制置为失败
#     
def test_ehlo_yield(smtp_connection_yield):
    response, _ = smtp_connection_yield.ehlo()
    assert response == 250
    assert 0  # 为了展示，强制置为失败
