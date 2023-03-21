import argparse
from typing import Final
import time
import paho.mqtt.client as mqtt
from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
from PIL import ImageFont

# Add command line arguments for setting config
parser = argparse.ArgumentParser()
parser.add_argument("--mqtt_host")
parser.add_argument("--mqtt_user")
parser.add_argument("--mqtt_password")
parser.add_argument("--message")
parser.add_argument("--display_type")
parser.add_argument("--display_rotate", type=int)
parser.add_argument("--display_interface_serial")
parser.add_argument("--display_interface_port", type=int)
parser.add_argument("--display_interface_address", type=int)
args = parser.parse_args()

# Set config options
MQTT_HOST: Final = args.mqtt_host
MQTT_USER: Final = args.mqtt_user
MQTT_PASSWORD: Final = args.mqtt_password
DISPLAY_TYPE: Final = args.display_type
DISPLAY_ROTATE: Final = args.display_rotate
DISPLAY_INTERFACE_SERIAL: Final = args.display_interface_serial
DISPLAY_INTERFACE_SERIAL_PORT: Final = args.display_interface_port
DISPLAY_INTERFACE_SERIAL_ADDRESS: Final = args.display_interface_address #0x3C

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("oled/message")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload, encoding="UTF-8"))
    with canvas(device) as draw:
        #draw.rectangle(device.bounding_box, outline="white", fill="black")
        device.clear()
        draw.text((1, 1), str(msg.payload, encoding="UTF-8"), font=fnt, fill="white")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=MQTT_USER, password=MQTT_PASSWORD)
client.connect(MQTT_HOST, 1883, 60)



# Create the interface the device is connected to. Currently i2c support only.
interface = globals()[DISPLAY_INTERFACE_SERIAL](port=DISPLAY_INTERFACE_SERIAL_PORT, address=DISPLAY_INTERFACE_SERIAL_ADDRESS)
# Create the display device
device = globals()[DISPLAY_TYPE](interface, rotate=DISPLAY_ROTATE)
device.contrast(50)

fnt = ImageFont.truetype("/usr/bin/SF-Compact.ttf", 40)

# Draw some text
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((1, 1), args.message, font=fnt, fill="white")

client.loop_forever()