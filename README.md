# Github API v3 wrapper

Demo project written in Python with the help of Sanic and aiottp.
This web app is capable of handling multiple requests at the same time since is built on asyncio.
If repository is not found, it will return an empty dictionary as string.
Do a simple GET request to the following address:
```
http://host:80/repositories/<github_username>/<repository>
```


## Getting Started
If you have all libraries/dependencies installed, run with this command:

```
python3 webserver.py
```

### Installing

You can run the full app through Docker.
If needed change port number or host with environmental variables
Built and run the image:
```
docker build .

docker run -p 80:80 app --net localhost

```

If you're not running with Docker, make sure to create a virtual environment and install all dependencies with pip as follows:

```
pip install -r requirements.txt
```

## Running the tests

Tests can be found on the /tests folder and run with Pytest framework.
Run from the main project folder:

```
sudo python -m pytest tests/
```

## Built With

* [Sanic](http://sanic.readthedocs.io)
* [aiohttp](https://aiohttp.readthedocs.io)
* [Docker](https://www.docker.com)

## Authors

* **Leonardo Silva Vilhena** - *Github user* - [Github](https://github.com/Leovilhena)
