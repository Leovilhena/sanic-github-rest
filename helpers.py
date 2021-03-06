import os

# -------------------------------------------------------------------- #
# Request variables
# -------------------------------------------------------------------- #
HEADERS = {
    'User-Agent': os.environ.get('USERNAME', 'Allegro - Github Parser'),
    'Time-Zone': 'Europe/Warsaw',
}

# -------------------------------------------------------------------- #
# Github credentials
# -------------------------------------------------------------------- #

GITHUB_USER = os.environ.get('USER', '')

# -------------------------------------------------------------------- #
# Web server network config
# -------------------------------------------------------------------- #

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', 80)
