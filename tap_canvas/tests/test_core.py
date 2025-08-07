"""Test core functionality."""

import pytest
from singer_sdk.testing import get_tap_test_class

from tap_canvas.tap import TapCanvas

SAMPLE_CONFIG = {
    "api_key": "test_key",
    "base_url": "https://test.canvas.instructure.com/api/v1",
}


TestTapCanvas = get_tap_test_class(
    tap_class=TapCanvas,
    config=SAMPLE_CONFIG
)


class TestTapCanvasCustom(TestTapCanvas):
    """Custom tests for Canvas tap."""
    
    def test_tap_initialization(self):
        """Test that the tap initializes correctly."""
        tap = TapCanvas(config=SAMPLE_CONFIG)
        assert tap.name == "tap-canvas"
        assert tap.config["api_key"] == "test_key"
        assert tap.config["base_url"] == "https://test.canvas.instructure.com/api/v1"
    
    def test_stream_discovery(self):
        """Test that streams are discovered correctly."""
        tap = TapCanvas(config=SAMPLE_CONFIG)
        streams = tap.discover_streams()
        assert len(streams) > 0
        
        stream_names = [stream.name for stream in streams]
        expected_streams = ["courses", "users", "enrollments"]
        
        found_streams = [name for name in expected_streams if name in stream_names]
        assert len(found_streams) > 0
    
    def test_capabilities(self):
        """Test that capabilities are properly defined."""
        tap = TapCanvas(config=SAMPLE_CONFIG)
        capabilities = tap.capabilities
        
        assert isinstance(capabilities, list), "Capabilities should be a list"
        assert len(capabilities) > 0, "Should have at least one capability"
        
        capability_strings = [str(cap) if hasattr(cap, 'value') else cap for cap in capabilities]
        expected_caps = ["about", "catalog", "discover"]
        
        found_caps = [cap for cap in expected_caps if cap in capability_strings]
        assert len(found_caps) > 0, f"Should have at least some expected capabilities. Found: {capability_strings}"