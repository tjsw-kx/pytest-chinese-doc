def test_parames(smtp_connection_params):
    response, _ = smtp_connection_params.ehlo()
    assert response == 250
