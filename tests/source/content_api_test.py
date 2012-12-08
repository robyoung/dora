from collections import namedtuple
import unittest
from mock import patch
from dora.source import content_api

class GetTest(unittest.TestCase):
  def create_response(self, status_code, json):
    return namedtuple("response", ["status_code", "json"])(status_code, json)

  @patch("requests.get")
  def test_get(self, get):
    get.return_value = self.create_response(200, "result")
    response = content_api.get("foo-bar")

    get.assert_called_once_with(
      "https://www.gov.uk/api/foo-bar.json"
    )
    self.assertEqual(response, "result")

  @patch("requests.get")
  def test_get_raises_with_non_200_status(self, get):
    get.return_value = self.create_response(500, "result")

    self.assertRaises(content_api.RequestFailure, content_api.get, "foo-bar")
