import unittest

from pyramid import testing


class TestHeartbeatView(unittest.TestCase):
    def test_view(self):
        from .views import heartbeat_view
        response = heartbeat_view(testing.DummyRequest())
        self.assertEquals({}, response)
