"""Light platform for telerupteur."""
from .const import (
    DEFAULT_NAME,
    DOMAIN,
    PLATFORMS,
    LIGHT,
    CONF_INPUT,
    CONF_OUTPUT,
    ICON,
    OUPTUT_DURATION,
)
import voluptuous as vol
import asyncio
import logging
from homeassistant.components.light import LightEntity, PLATFORM_SCHEMA
from homeassistant.util import slugify
from homeassistant.helpers import entity_platform
from homeassistant.helpers.reload import async_setup_reload_service
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.event import (
    async_track_state_change,
    async_track_time_interval,
)
from homeassistant.core import DOMAIN as HA_DOMAIN, callback
from homeassistant.const import (
    ATTR_ENTITY_ID,
    CONF_NAME,
    CONF_UNIQUE_ID,
    SERVICE_TURN_OFF,
    SERVICE_TURN_ON,
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_OUTPUT): cv.entity_id,
        vol.Required(CONF_INPUT): cv.entity_id,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_UNIQUE_ID, default="none"): cv.string,
    }
)

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the telerupteur platform."""
    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)

    platform = entity_platform.current_platform.get()
    assert platform

    parameters = {
        "name": config.get(CONF_NAME),
        "unique_id": config.get(CONF_UNIQUE_ID),
        "light_command_id": config.get(CONF_OUTPUT),
        "light_state_id": config.get(CONF_INPUT),
    }

    telerupteur = TelerupteurLight(**parameters)
    async_add_entities([telerupteur])


class TelerupteurLight(LightEntity):
    """Telerupteur light class."""

    def __init__(self, **kwargs):
        self._name = kwargs.get("name")
        self._unique_id = kwargs.get("unique_id")
        self._light_command_id = kwargs.get("light_command_id")
        self._light_state_id = kwargs.get("light_state_id")
        self._light_s = False
        if self._unique_id == "none":
            self._unique_id = slugify(f"{DOMAIN}_{self._name}_{self._light_command_id}")

    async def async_added_to_hass(self):
        """Run when entity about to be added."""
        await super().async_added_to_hass()

        # Add listener to check if light state has changed
        async_track_state_change(
            self.hass, self._light_state_id, self._async_light_changed
        )

    async def _async_light_changed(self, entity_id, old_state, new_state):
        """Handle Light State changes."""
        if new_state is None:
            return
        new_state = new_state.state

        if old_state is not None:
            old_state = old_state.state

        _LOGGER.debug("Light state change from %s to %s", old_state, new_state)
        self._light_s = new_state
        await self.async_update_ha_state()

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name}_{LIGHT}"

    @property
    def is_on(self):
        """Returns if the light entity is on or not."""
        if self._light_s is "on":
            return True
        return False

    @property
    def state(self):
        """Returns state of the light."""
        return self._light_s

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    async def _toggle_light(self):
        data = {ATTR_ENTITY_ID: self._light_command_id}
        await self.hass.services.async_call(HA_DOMAIN, SERVICE_TURN_ON, data)
        await asyncio.sleep(OUPTUT_DURATION)
        await self.hass.services.async_call(HA_DOMAIN, SERVICE_TURN_OFF, data)

    async def async_turn_on(self, **kwargs):
        """Turn device on."""
        await self._toggle_light()

    async def async_turn_off(self, **kwargs):
        """Turn device off."""
        await self._toggle_light()
