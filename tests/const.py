"""Constants for integration_blueprint tests."""
from custom_components.telerupteur.const import (
    DEFAULT_NAME,
    DOMAIN,
    LIGHT,
    CONF_INPUT,
    CONF_OUTPUT,
)

# Mock config data to be used across multiple tests
MOCK_CONFIG = {CONF_INPUT: "test_input_id", CONF_OUTPUT: "test_output_id"}
