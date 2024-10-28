import os
import tempfile

import pytest
import smtplib

@pytest.fixture(scope='module')
def smtp_connection_package():
    return smtplib.SMTP("smtp.163.com", 25, timeout=5)

@pytest.fixture(scope='package')
def smtp_connection_package():
    return smtplib.SMTP("smtp.163.com", 25, timeout=5)

@pytest.fixture()
def smtp_connection_yield():
    smtp_connection = smtplib.SMTP("smtp.163.com", 25, timeout=5)
    yield smtp_connection
    print("关闭SMTP连接")
    smtp_connection.close()

@pytest.fixture
def smtp_connection_fin(request):
    smtp_connection = smtplib.SMTP("smtp.163.com",25, timeout=5)

    def fin():
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection

@pytest.fixture(scope='module')
def smtp_connection_request(request):
    server,port = getattr(request.module,'smtp_server',("smtp.163.com",25))
    with smtplib.SMTP(server, port, timeout=5) as smtp_connection:
        yield smtp_connection
        print(f"断开 {server}:{port}")


@pytest.fixture()
def cleandir():
    newpath = tempfile.mktemp()
    os.chdir(newpath)
    
