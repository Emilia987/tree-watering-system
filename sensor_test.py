import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# initialize soil moisture sensor
moisture_pin = 15
GPIO.setup(moisture_pin, GPIO.IN)

# initialize temperature and humidity sensor
dht11_pin = 16
dht11_instance = dht11.DHT11(pin=dht11_pin)

# read sensors
for i in range(10):
    # read soil moisture sensor
    moisture_value = GPIO.input(moisture_pin)
    print("Soil moisture:", moisture_value)

    # read DHT11 sensor
    dht11_result = dht11_instance.read()
    if dht11_result.is_valid():
        temperature = dht11_result.temperature
        humidity = dht11_result.humidity
        print("Temperature: %d C" % temperature)
        print("Humidity: %d %%" % humidity)

    time.sleep(1)

# cleanup GPIO
GPIO.cleanup()
