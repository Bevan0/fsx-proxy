# FSX Proxy
FSX Proxy is a UDP proxy I created for Flight Simulator X.

## Installation
* Install [Python 3](python.org/downloads)

## Usage with FSX and playit.gg
The host should follow these instructions: (note: the host does not need FSX Proxy, only the players do)
* Go to [playit.gg](playit.gg) and download it.
* Create a tunnel on local port :6112.
* Get the IPv4 address (NOT THE DOMAIN! it should look like 123.123.123.123) and assigned port.
* Give those details to players.

Players should follow these instructions:
* Open `settings.py` and set the settings.
* SERVER_LINK should be set to the IPv4 address and port of the playit.gg tunnel, as provided by the host.
* Run `python proxy.py` to start the proxy.

## Configuration
The settings file is `settings.py`.