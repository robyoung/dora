import os
import json
import requests
import urllib

from dora import source

CREDENTIALS_FILE = os.path.join(source.AUTH_PATH, "zendesk.json")
ZENDESK_URL = 'https://govuk.zendesk.com'


def authenticate(username, password):
    with open(CREDENTIALS_FILE, 'w+') as f:
        json.dump({"username": username, "password": password}, f)


def _credentials():
    with open(CREDENTIALS_FILE) as f:
        return json.load(f)


def client(api_version):
    credentials = _credentials()

    return Zendesk(
        ZENDESK_URL,
        credentials['username'],
        credentials['password'],
        api_version = api_version
    )


class Zendesk(object):
    def __init__(self, base_url, username, password, api_version):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.api_version = api_version

    def url(self, path, args):
        return '{0}/api/v{1}/{2}.json?{3}'.format(
            self.base_url,
            self.api_version,
            path,
            urllib.urlencode(args)
        )

    def get(self, path, **kwargs):
        auth = (self.username, self.password)
        url  = self.url(path, kwargs)
        resp = requests.get(url, auth=auth)
        resp.raise_for_status()
        return resp.json()
