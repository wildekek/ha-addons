# Home Assistant Add-on: MIDIMonster

## How to use

This add-on expects a configuration file to live at /config/midimonster/midimonster.cfg
See: https://midimonster.net/getStarted.html#creating-a-new-configuration

(This config should be moved to the config tab in HA)

### Example:
```
[backend midi]
name = HomeAssistant
detect = on

[backend mqtt]

[midi esx]
read = ESI MIDIMATE eX:1
write = ESI MIDIMATE eX:0
epn-tx = short

[mqtt homeassistant]
host =	mqtt://addon_core_mosquitto
user = addons
password = mypass
clientid = midimonster-hass
protocol = 5

[map]
homeassistant.midi2mqtt/midi_out/channel/{0..15}/note/{0..127} > esx.ch{0..15}.note{0..127}
esx.ch{0..15}.note{0..127} > homeassistant.midi2mqtt/midi_in/channel/{0..15}/note/{0..127}
```
