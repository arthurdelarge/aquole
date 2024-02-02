import glob
import time
from kafka import KafkaProducer, KafkaConsumer
import math
import threading
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from const import *

# For access to the acceleration sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER+':'+KAFKA_PORT)
last_reported_acc = 0
last_reported_light_level = 0

def read_acc_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_acc():
    lines = read_acc_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_acc_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        acc_string = lines[1][equals_pos+2:]
        acc_c = float(acc_string) / 1000.0
        acc_f = acc_c * 9.0 / 5.0 + 32.0
        return acc_c, acc_f

def read_light_sensor (pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

while True:
    # Read and report acceleration to the cloud-based service
    (acc_c, acc_f) = read_acc()
    print('Acceleration: ', acc_c, acc_f)
    if (math.fabs(acc_c - last_reported_acc) >= 0.1):
        last_reported_acc = acc_c
        producer.send('acceleration', str(acc_c).encode())

    # Read and report light lelve to the cloud-based service
    light_level = read_light_sensor(light_sensor_pin)
    print('Light level: ', light_level)
    if (light_level != last_reported_light_level):
        last_reported_light_level = light_level
        producer.send('lightlevel', str(light_level).encode())
    time.sleep(1)
