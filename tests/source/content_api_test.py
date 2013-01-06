from collections import namedtuple
import unittest
from mock import patch
from dora.source import content_api

def create_response(status_code, json):
  return namedtuple("response", ["status_code", "json"])(status_code, json)

class UrlTest(unittest.TestCase):
  def test_url(self):
    self.assertEqual(content_api.url("foo-bar"), "https://www.gov.uk/api/foo-bar.json")
    self.assertEqual(content_api.url("https://www.gov.uk/api/foo-bar.json"), "https://www.gov.uk/api/foo-bar.json")

class GetTest(unittest.TestCase):
  @patch("requests.get")
  def test_get(self, get):
    get.return_value = create_response(200, "result")
    response = content_api.get("foo-bar")

    get.assert_called_once_with(
      "https://www.gov.uk/api/foo-bar.json"
    )
    self.assertEqual(response, "result")

  @patch("requests.get")
  def test_get_should_allow_full_url(self, get):
    get.return_value = create_response(200, "result")
    response = content_api.get("https://www.gov.uk/api/foo-bar.json")

    get.assert_called_once_with(
      "https://www.gov.uk/api/foo-bar.json"
    )
    self.assertEqual(response, "result")

  @patch("requests.get")
  def test_get_raises_with_non_200_status(self, get):
    get.return_value = create_response(500, "result")

    self.assertRaises(content_api.RequestFailure, content_api.get, "foo-bar")

class ArtefactsTest(unittest.TestCase):
  @patch("dora.source.content_api.get")
  def test_artefacts(self, get):
    responses = {
      "artefacts": {
        "results":[
          {"id":"https://www.gov.uk/book-life-in-uk-test.json"},
          {"id":"https://www.gov.uk/bullying-at-school.json"}
        ]
      },
      "https://www.gov.uk/book-life-in-uk-test.json": "book life in uk test",
      "https://www.gov.uk/bullying-at-school.json": "bullying at school"
    }
    get.side_effect = lambda slug: responses[slug]

    artefacts = list(content_api.artefacts())
    self.assertEqual(len(artefacts), 2)
    self.assertEqual(artefacts[0], "book life in uk test")
    self.assertEqual(artefacts[1], "bullying at school")