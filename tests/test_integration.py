from webserver import APP

TEST_REPOSITORY = '/Leovilhena/test-repository'


def test_webserver():
    params = {'client_id': 'test_id', 'client_key': 'test_key'}
    request, response = APP.test_client.get(TEST_REPOSITORY, params=params)

    assert response.method == 'GET'
    assert response.status == 200
    assert request.args.get('client_id') == 'test_id'
    assert request.args.get('client_key') == 'test_key'
