#dependancy: Paho-mqtt

from datetime import datetime
import paho.mqtt.client as mqtt

#Default broker port is 1883
broker_port = 1883
#Enter IP where the broker resides
broker_address = "192.168.1.1"
username = "Your_username"
password = "YourPW_or_env_variable"


def on_connect(client, userdata, flags, rc):
	print("Connected: " + str(rc))

def on_message(client, userdata, message):
	currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
	print(currentTime + message.payload.decode())

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker_address, broker_port)

client.subscribe("temperature")
client.on_message = on_message
client.on_connect = on_connect

client.loop_forever()
