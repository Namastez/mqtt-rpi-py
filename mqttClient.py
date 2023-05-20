#Dependancy: paho-mqtt
#Install with pip install paho-mqtt

import paho.mqtt.client as mqtt
import os
import time




#What IP the broker is located at
broker_address = "192.168.1.1" 
#Default port is 1883
broker_port = 1883
username = "user"

#Create a environmentable variable with:
#export MQTT_PW_VARIABLE="PasswordToSave"
password = os.environ.get('MQTT_PW_VARIABLE')


def main():
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.connect(broker_address, broker_port)


    while True:
        temp = os.popen("vcgencmd measure_temp").readline()
        temp_info = "Raspberry temp: " +  temp[5:]
        client.publish("temperature", temp_info)
        time.sleep(30)

    client.loop_stop()
    client.disconnect()


if __name__ == '__main__':
    main()
