import requests

class RequestFailure(StandardError):
  def __init__(self, response, message):
    super(RequestFailure, self).__init__(message)
    self._response = response

  @property
  def response(self):
    return self._response

def url(slug):
  if slug.startswith("https://"):
    return slug
  else:
    return "https://www.gov.uk/api/%s.json" % slug

def get(slug):
  full_url = url(slug)
  response = requests.get(full_url)
  if response.status_code != 200:
    raise RequestFailure(response, "Invalid response code")
  return response.json

def artefacts():
  results = get("artefacts")
  for artefact in results["results"]:
    yield get(artefact["id"])