import unittest
from datetime import date, datetime
from mock import Mock
from dora.source.google_analytics import QueryClient, QueryResponse

class QueryClientTest(unittest.TestCase):
  def test_query_calls_provided_client(self):
    service_client = Mock()
    service_client.query.return_value = "raw result"

    profile_id = "1234"
    client = QueryClient(service_client, profile_id)

    client.query(
      date(2012, 11, 1),
      date(2012, 11, 5),
      "metric1",
      "dimension"
    )

    service_client.query.assert_called_once_with(
      profile_id,
      date(2012, 11, 1), date(2012, 11, 5),
      "metric1", "dimension"
    )


class QueryResponseTest(unittest.TestCase):
  def test_raw_value(self):
    response = QueryResponse("foo")
    self.assertEqual(response.raw, "foo")

  def test_can_iterate_over_response(self):
    response = QueryResponse([
      "foo", "bar"
    ])
    results = list(response)
    self.assertEqual(len(results), 2)

  def test_iterated_items(self):
    response = QueryResponse([
        {"metrics": {"visits": 1000, "visitors": 2000}, "dimensions": {"week": "46"}, "start_date": date(2012, 12, 12)}
    ])

    results = list(response)
#    self.assertEqual(results[0].start_at, datetime(2012, 12, 12))

