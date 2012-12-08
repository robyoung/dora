import requests

class RequestFailure(StandardError):
  def __init__(self, response, message):
    super(RequestFailure, self).__init__(message)
    self._response = response

  @property
  def response(self):
    return self._response

def get(slug):
  response = requests.get("https://www.gov.uk/api/%s.json" % slug)
  if response.status_code != 200:
    raise RequestFailure(response, "Invalid response code")
  return response.json