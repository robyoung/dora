import os
import json

from dora import source

CREDENTIALS_FILE = os.path.join(source.AUTH_PATH, "zendesk.json")


def authenticate(username, password):
    with open(CREDENTIALS_FILE, 'w+') as f:
        json.dump({"username":username, "password":password}, f)