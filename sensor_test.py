import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Set up the soil moisture sensor on pin 15
GPIO.setup(15, GPIO.IN)

# Set up the DHT11 temperature and humidity sensor on pin 16
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 16

# Read data from both sensors 10 times
for i in range(10):
    # Read soil moisture sensor data
    soil_moisture = GPIO.input(15)
    
    # Read DHT11 temperature and humidity data
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # Print data to console
    print("Soil moisture: ", soil_moisture)
    print("Temperature: ", temperature)
    print("Humidity: ", humidity)
    
    # Delay for 2 seconds to allow sensors to stabilize
    time.sleep(2)

# Clean up GPIO pins
GPIO.cleanup()
