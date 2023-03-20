# Home Assistant Add-on: MIDIMonster

## TODO:
- Fix path dependency when starting outside of source dir
- Create a MidiMonster config from the hass container config.
- Replace the mqtt credentials in the config with mqqt variables (see run file)
- Make read and write ports come from config
- Remove the need for unprotected mode
- Add apparmor config

## Instructions:
This add-on expects a configuration file to live at /config/midimonster/midimonster.cfg
See: https://midimonster.net/getStarted.html#creating-a-new-configuration

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


![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-no-red.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-no-red.svg
