"""Constants for integration_blueprint."""
# Base component constants
NAME = "Telerupteur"
DOMAIN = "telerupteur"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "2021.12.8"
ISSUE_URL = "https://github.com/custom-components/ha-telerupteur-component/issues"

LIGHT = "light"
PLATFORMS = [LIGHT]

# Defaults
DEFAULT_NAME = DOMAIN

CONF_OUTPUT = "light_command"
CONF_INPUT = "light_state"

OUPTUT_DURATION = 1

ICON = "mdi:lightbulb"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
