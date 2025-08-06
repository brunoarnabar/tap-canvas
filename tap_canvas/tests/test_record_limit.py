"""Test record limit configuration."""

from tap_canvas.client import CanvasStream
from singer_sdk import typing as th


class DummyStream(CanvasStream):
    name = "dummy"
    path = "/dummy"
    primary_keys = ["id"]
    schema = th.PropertiesList(th.Property("id", th.IntegerType)).to_dict()


class DummyResponse:
    """Simple response stub with JSON payload."""

    def __init__(self):
        self.links = {}
        self._json = [{"id": 1}, {"id": 2}, {"id": 3}]

    def json(self):
        return self._json


def test_record_limit_applied():
    stream = DummyStream(
        tap=None,
        config={"base_url": "http://example", "api_key": "x", "record_limit": 2},
    )
    records = list(stream.parse_response(DummyResponse()))
    assert len(records) == 2
    # After hitting limit, there should be no next page token even if provided
    token = stream.get_next_page_token(DummyResponse(), None)
    assert token is None
