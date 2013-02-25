import os
from pandas.io.ga import read_ga as pandas_read_ga
from dora import source


SECRETS=os.path.join(source.AUTH_PATH, "client_secrets.json")
TOKEN_FILE_NAME=os.path.join(source.AUTH_PATH, "analytics.dat")


def authenticate():
  import BaseHTTPServer
  import sys
  from oauth2client.client import flow_from_clientsecrets
  from oauth2client.file import Storage
  from pandas.io.auth import DEFAULT_SCOPE
  from urlparse import parse_qsl

  flow = flow_from_clientsecrets(SECRETS, scope=DEFAULT_SCOPE, redirect_uri="http://localhost:8080")
  storage = Storage(TOKEN_FILE_NAME)

  class ClientRedirectServer(BaseHTTPServer.HTTPServer):
    query_params = {}

  class ClientRedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
      s.send_response(200)                                                                             
      s.send_header("Content-type", "text/html")
      s.end_headers()
      query = s.path.split('?', 1)[-1]
      query = dict(parse_qsl(query))
      s.server.query_params = query
      response = """
<html>
<head><title>Authentication Status</title></head>
<body>
<p>The authentication flow has completed.</p>
<p>You can now close this tab.</p>
</body>
</html>
"""
      s.wfile.write(response)

    def log_message(self, format, *args):
      pass

  httpd = ClientRedirectServer(("0.0.0.0", 8080), ClientRedirectHandler)

  authorize_url = flow.step1_get_authorize_url()

  print "Go to the following link in your browser"
  print authorize_url

  sys.stdout.flush()

  httpd.handle_request()
  if "error" in httpd.query_params:
    raise Exception("ERROR: auth failed")
  if "code" in httpd.query_params:
    code = httpd.query_params["code"]
  else:
    print httpd.query_params

  credentials = flow.step2_exchange(code)
  storage.put(credentials)

def read_ga(metrics, dimensions, start_date, **kwargs):
    """
    Wrapper for pandas.io.ga.read_ga that set the secrets and token file
    """
    if 'secrets' not in kwargs:
        kwargs['secrets'] = SECRETS
    if 'token_file_name' not in kwargs:
        kwargs['token_file_name'] = TOKEN_FILE_NAME

    return pandas_read_ga(metrics, dimensions, start_date, **kwargs)