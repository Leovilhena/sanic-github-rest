import aiohttp
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import ServerError, NotFound
from helpers import *

# -------------------------------------------------------------------- #
# Global variables
# -------------------------------------------------------------------- #

APP = Sanic()


# -------------------------------------------------------------------- #
# App functions
# -------------------------------------------------------------------- #

def github_parse(data):
    """Parse json response data from Github API v3

    :param data: json object fetched from Github API v3
    :return: dict with parsed information as strings
    """

    try:
        parsed_results = {
            'fullName': data.get('full_name', ''),
            'description': data.get('description', ''),
            'cloneUrl': data.get('clone_url', ''),
            'stars': data.get('stargazers_count', 0),
            'createdAt': data.get('created_at', '')
        }

        return parsed_results
    except (ValueError, AttributeError):
        return {}


async def github_fetch(session, url, params):
    """Create an HTTP request to Github API v3

    :param session: aiohttp HTTP session object
    :param url: url to be fetched
    :param params: query string variables
    :return: json data
    """

    try:
        async with session.get(url, params=params) as result:
            return await result.json()
    except aiohttp.client_exceptions.InvalidURL:
        raise ServerError({}, status_code=500)


@APP.route('/repositories/<owner>/<repository_name>')
async def main_route(request, owner, repository_name):
    """Route requests from clients according to their Github owner and repository name

    :param request: HTTP Request object
    :param owner: github account name
    :param repository_name: github repository name
    :return: parsed dictionary response as a string
    """

    url = 'https://api.github.com/repos/{}/{}'.format(owner, repository_name)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        raw_data = await github_fetch(session, url, request.raw_args)
        parsed_data = github_parse(raw_data)
        return text(parsed_data)


@APP.exception(NotFound)
def standard_error(request, exception):
    return text({})


if __name__ == "__main__":
    APP.run(
        host=HOST,
        port=PORT,
        workers=WORKERS
    )
