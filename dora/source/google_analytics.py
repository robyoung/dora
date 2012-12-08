import itertools

class QueryClient(object):
  def __init__(self, client, profile_ids):
    self._client = client
    self._profile_ids = profile_ids

  def query(self, *args, **kwargs):
    return QueryResponse(
      self._client.query(self._profile_ids, *args, **kwargs)
    )

class QueryResponse(object):
#  class Item(object):
#    def __init__(self, value):
#      self._value = value

  def __init__(self, response):
    self._response = response

  @property
  def raw(self):
    return self._response

  def __iter__(self):
    return itertools.imap(self._parse_row, self._response)

  def _parse_row(self, row):
    # is it weekly
    return row
