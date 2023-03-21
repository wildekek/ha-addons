# Home Assistant Add-on: OLED add-on

## How to use

### Enable i2c on your Pi
Your OLED display is most likely connected via i2c. Please make sure it is available to HA:
https://community.home-assistant.io/t/add-on-hassos-i2c-configurator/264167


### Configuration
Set your display settings in the configuration and start the add-on. If you see no errors in the logs,you should be set.
Currently this add-on only supports the sh1106 screen, but it should be very easy to add the other supported displays:https://luma-oled.readthedocs.io/en/latest/

### Usage
You can try to send a MQTT message to the topic oled/message and it should show on your screen!