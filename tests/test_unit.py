import pytest
import aiohttp
from sanic.response import json
from helpers import HEADERS, HOST, PORT
from webserver import APP, github_parse, github_fetch


# -------------------------------------------------------------------- #
# Global variables
# -------------------------------------------------------------------- #

TEST_DATA = {
    u'clone_url': u'https://github.com/test/test.git',
    u'created_at': u'2018-06-25T18:03:55Z',
    u'description': u'Test mock',
    u'full_name': u'test/test',
    u'stargazers_count': 4,
    u'test_key': None,
}

EXPECTED_DATA = {
    'fullName': u'test/test',
    'description': u'Test mock',
    'cloneUrl': u'https://github.com/test/test.git',
    'stars': 4,
    'createdAt': u'2018-06-25T18:03:55Z'
}

ROUTE_ADDRESS = '/repositories/test/test'

# -------------------------------------------------------------------- #
# Test cases
# -------------------------------------------------------------------- #


def test_github_parse():
    assert type(github_parse(TEST_DATA)) is dict
    assert github_parse(TEST_DATA) == EXPECTED_DATA

    keys = ['fullName', 'description', 'cloneUrl', 'stars', 'createdAt']
    assert list(github_parse({}).keys()) == keys
    assert github_parse('') == {}


# Route created for test GET request
@APP.route(ROUTE_ADDRESS)
def mocked_route(request):
    return json('ok')


@pytest.mark.asyncio
async def test_github_fetch():
    await APP.create_server(host=HOST, port=PORT)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        url_test = ''.join(['http://', HOST, ':', str(PORT), ROUTE_ADDRESS])
        results = await github_fetch(session, url_test, params={})
        assert results == 'ok'

    APP.stop()

