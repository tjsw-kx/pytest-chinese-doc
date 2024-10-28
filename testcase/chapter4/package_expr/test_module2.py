def test_ehlo_in_module2(smtp_connection_package):
    response, _ = smtp_connection_package.ehlo()
    assert response == 250
    assert 0  # 为了展示，强制置为失败
