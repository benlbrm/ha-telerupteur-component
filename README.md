[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]


**This component will set up the following platforms.**

Platform | Description
-- | --
`light` | Light control with a telerupteur.


## Installation

1. Add this repository to HACS.
2. Click install.


## Configuration is done in the configuration.yaml
```yaml
light:
- platform: telerupteur
    name: Lumiere Chambre1
    light_command: switch.dolightchambre1
    light_state: binary_sensor.dilightchambre1
```

## Required hardware to use this integration

- Telerupteur to control lights with push buttons [[telerupteur-link]][link]
- 24Vdc to 230Vac relay to control the telerupteur, this relay is wired like a push button
- 230Vac to 24vdc relay to get the light status, this relay is wired like a light

<!---->

***

[integration_telerupteur]: https://github.com/benlbrm/ha-telerupteur-component
[buymecoffee]: https://www.buymeacoffee.com/benlbrm
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/benlbrm/ha-telerupteur-component.svg?style=for-the-badge
[commits]: https://github.com/benlbrm/ha-telerupteur-component/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/benlbrm/ha-telerupteur-component/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/benlbrm/ha-telerupteur-component.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-benlbrm-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/benlbrm/ha-telerupteur-component.svg?style=for-the-badge
[releases]: https://github.com/benlbrm/ha-telerupteur-component/releases
[user_profile]: https://github.com/benlbrm
[telerupteur-link]: https://www.legrand.fr/catalogue/contacteur-minuterie-parafoudre/telerupteur-unipolaire-230v-16a-1-module
