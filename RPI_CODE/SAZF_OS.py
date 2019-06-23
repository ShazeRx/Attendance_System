from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106


''''Now only basic data'''


device_id= 'terminal-1'
project_id='gassist-232317'
cloud_region='us-central1'
registry_id='terminal'
private_key_file='rsa_private.pem'
alghoritm='RS256'
ca_certs='roots.pem'
mqtt_bridge_hostname='mqtt.googleapis.com'
mqtt_bridge_port=8883

serial = i2c(port=1, address=0x3C)
import ssl
import jwt
import datetime
import time
import random
import logging
import ast
# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)
import paho.mqtt.client as mqtt
pn532 = Pn532_i2c()
pn532.SAMconfigure()
from time import sleep
pin = 18
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
mqtt.Client.connected_flag=False
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.CRITICAL)

card_id=''
# The initial backoff time after a disconnection occurs, in seconds.
minimum_backoff_time = 1

# The maximum backoff time before giving up, in seconds.
MAXIMUM_BACKOFF_TIME = 32

# Whether to wait with exponential backoff before publishing.
should_backoff = False


def dump():
    pass


device.cleanup=dump
def error_str(rc):
    """Convert a Paho error to a human readable string."""
    return '{}: {}'.format(rc, mqtt.error_string(rc))


def on_connect(client, unused_userdata, unused_flags, rc):
    """Callback for when a device connects."""
    print('on_connect', mqtt.connack_string(rc))
    # After a successful connect, reset backoff time and stop backing off.
    global should_backoff
    global minimum_backoff_time
    should_backoff = False
    minimum_backoff_time = 1


def on_disconnect(unused_client, unused_userdata, rc):
    """Paho callback for when a device disconnects."""
    print('on_disconnect', error_str(rc))

    # Since a disconnect occurred, the next loop iteration will wait with
    # exponential backoff.
    global should_backoff
    should_backoff = True


def on_publish(unused_client, unused_userdata, unused_mid):
    """Paho callback when a message is sent to the broker."""
    print('on_publish')
def on_message(unused_client, unused_userdata, message):
    """Callback when the device receives a message on a subscription."""
    payload = str(message.payload)
    mesg_dict = ast.literal_eval(payload)
    print(mesg_dict)

def create_jwt(project_id,private_key_file,alghoritm):
    """Creates a JWT (https://jwt.io) to establish an MQTT connection.
            Args:
             project_id: The cloud project ID this device belongs to
             private_key_file: A path to a file containing either an RSA256 or
                     ES256 private key.
             algorithm: The encryption algorithm to use. Either 'RS256' or 'ES256'
            Returns:
                An MQTT generated from the given project_id and private key, which
                expires in 20 minutes. After 20 minutes, your client will be
                disconnected, and a new JWT will have to be generated.
            Raises:
                ValueError: If the private_key_file does not contain a known key.
            """

    token = {
        # The time that the token was issued at
        'iat': datetime.datetime.utcnow(),
        # The time the token expires.
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        # The audience field should always be set to the GCP project id.
        'aud': project_id
    }

    # Read the private key file.
    with open(private_key_file, 'r') as f:
        private_key = f.read()

    print('Creating JWT using {} from private key file {}'.format(
        alghoritm, private_key_file))

    return jwt.encode(token, private_key, algorithm=alghoritm)


def get_client(
        project_id, cloud_region, registry_id, device_id, private_key_file,
        algorithm, ca_certs, mqtt_bridge_hostname, mqtt_bridge_port):
    """Create our MQTT client. The client_id is a unique string that identifies
    this device. For Google Cloud IoT Core, it must be in the format below."""
    client_id = ('projects/{}/locations/{}/registries/{}/devices/{}'
        .format(
        project_id,
        cloud_region,
        registry_id,
        device_id))
    print(client_id)
    client = mqtt.Client(client_id)

    # With Google Cloud IoT Core, the username field is ignored, and the
    # password field is used to transmit a JWT to authorize the device.
    client.username_pw_set(
        username='unused',
        password=create_jwt(
            project_id, private_key_file, algorithm))

    # Enable SSL/TLS support.
    client.tls_set(ca_certs=ca_certs, tls_version=ssl.PROTOCOL_TLSv1_2)

    # Register message callbacks. https://eclipse.org/paho/clients/python/docs/
    # describes additional callbacks that Paho supports. In this example, the
    # callbacks just print to standard out.
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    # Connect to the Google MQTT bridge.
    client.connect(mqtt_bridge_hostname, mqtt_bridge_port)

    # This is the topic that the device will receive configuration updates on.
    mqtt_config_topic = '/devices/{}/config'.format(device_id)

    # Subscribe to the config topic.
    client.subscribe(mqtt_config_topic, qos=1)

    # The topic that the device will receive commands on.
    mqtt_command_topic = '/devices/{}/commands/#'.format(device_id)

    # Subscribe to the commands topic, QoS 1 enables message acknowledgement.
    print('Subscribing to {}'.format(mqtt_command_topic))
    client.subscribe(mqtt_command_topic, qos=0)

    return client
def read_tag():
    print("Waiting for tags")
    device.clear()

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Waiting for tag", fill="white")

    card_data = pn532.read_mifare().get_data()
    card_data = int.from_bytes(card_data, byteorder='big')

    GPIO.output(pin, True)
    time.sleep(0.5)
    GPIO.output(pin, False)


    print(card_data)
    device.clear()

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), str(card_data), fill="white")
    return str(card_data)







def main():
    global card_id
    """Connects a device, sends data, and receives data."""
    # [START iot_mqtt_run]
    global minimum_backoff_time
    global MAXIMUM_BACKOFF_TIME
    sub_topic = 'events'
    mqtt_topic = '/devices/{}/{}'.format(device_id, sub_topic)
    jwt_iat = datetime.datetime.utcnow()
    jwt_exp_mins = 120
    client = get_client(
        project_id, cloud_region, registry_id,
        device_id, private_key_file, alghoritm,
        ca_certs, mqtt_bridge_hostname, mqtt_bridge_port)
    client.loop_start()
    while True:

        # Wait if backoff is required.
        if should_backoff:
            # If backoff time is too large, give up.
            if minimum_backoff_time > MAXIMUM_BACKOFF_TIME:
                print('Exceeded maximum backoff time. Giving up.')
                break

            # Otherwise, wait and connect again.
            delay = minimum_backoff_time + random.randint(0, 1000) / 1000.0
            print('Waiting for {} before reconnecting.'.format(delay))
            time.sleep(delay)
            minimum_backoff_time *= 2
            client.connect(mqtt_bridge_hostname,mqtt_bridge_port)

        print("Ready to scan card")
        card_id = read_tag()
        payload = '{"Card":"' + card_id + '"}'
        print('Publishing message : \'{}\''.format(payload))
        # [START iot_mqtt_jwt_refresh]
        seconds_since_issue = (datetime.datetime.utcnow() - jwt_iat).seconds
        if seconds_since_issue > 60 * jwt_exp_mins:
            print('Refreshing token after {}s').format(seconds_since_issue)
            jwt_iat = datetime.datetime.utcnow()
            client = get_client(
                project_id, cloud_region,
                registry_id, device_id,private_key_file,
                alghoritm, ca_certs,mqtt_bridge_hostname,
                mqtt_bridge_port)
            client.loop_start()
        # [END iot_mqtt_jwt_refresh]
        # Publish "payload" to the MQTT topic. qos=1 means at least once
        # delivery. Cloud IoT Core also supports qos=0 for at most once
        # delivery.
        client.publish(mqtt_topic, payload, qos=1)

        # Send events every second. State should not be updated as often
        time.sleep(1)



if __name__ == '__main__':
    main()
