# Home Assistant Add-on: MIDIMonster

## About
This add-on allow you to use [MIDIMonster](https://midimonster.net/) inside Home Assistant.
Currently it supports MIDI and MQTT as backends, so you can translate a MQTT message into a MIDI command and vice-versa.

## TODO:
- Fix path dependency when starting outside of source dir
- Create a MidiMonster config from the hass container config.
- Replace the mqtt credentials in the config with mqqt variables (see run file)
- Make read and write ports come from config
- Remove the need for unprotected mode
- Add apparmor config

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
