# Snips Fritz!Box connector
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/snipsco/snips-skill-owm/master/LICENSE.txt)

This is a Snips action to interact with an AVM Fritz!Box router/PBX. It is written in Python and is compatible with `snips-skill-server`.

## Setup
### Prerequisites

You'll need to add the Fritz!Connect skill in your assistant. It's available on [Snips' console](https://console.snips.ai)

You'll also need to make sure some development packages are installed on your system:
`python-dev , libxml2-dev , libxslt-dev`

On Raspian you can isntall this via `sudo apt-get install python-dev libxml2-dev libxslt-dev`

### SAM (preferred)
To install the action on your device, you can use [Sam](https://snips.gitbook.io/getting-started/installation)

`sam install actions -g https://github.com/shilbert01/snips-skill-fritz-connect.git`

### Manually

Copy it manually to the device to the folder `/var/lib/snips/skills/`
You'll need `snips-skill-server` installed on the pi

`sudo apt-get install snips-skill-server`

Stop snips-skill-server & generate the virtual environment
```
sudo systemctl stop snips-skill-server
cd /var/lib/snips/skills/snips-skill-fritz-connect/
sh setup.sh
sudo systemctl start snips-skill-server
```

## How to trigger

`Hey Snips`

`Rufe Opa an.`

## Logs
Show snips-skill-server logs with sam:

`sam service log snips-skill-server`

Or on the device:

`journalctl -f -u snips-skill-server`

Check general platform logs:

`sam watch`

Or on the device:

`snips-watch`
