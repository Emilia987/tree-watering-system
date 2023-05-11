# tree-watering-system

Project Discription:

Project Goals: To make a program that controls a pump and takes data from multiple sensors. The program is supposed to take the sensor data and per settings that are customizable by the user, it's supposed to turn on the pump. 
For example, when the user sets the water to turn on at 50% ground moisture and outside temperature of over 20°C, the pump should turn on.  It's important that both of the ground and air sensor have an n/a option, which makes sure that they aren't included for current configuration, if the user so chooses. 
Along with the basic program, I want to make a small and simple webpage that will be hosted locally on the raspberry pi. This webpage is supposed to have a monitoring function, where things like the temperature of the raspberry pi, the temperature and humidity outside and the humidity of the soil are all visible at a glance. Also I want a settings page for it that allows the user to enter profiles and make routines for how often and at what humidity, temperature the system is supposed to turn on the pump to water the tree. A login screen of sorts would also be nice, considering this thing will always have a wifi signal with a webpage anyone could go into.

Parts List:
-USB waterpump: A small USB powered waterpump that is supposed to be plugged into and controlled by the raspi directly. The code just needs a function for turning the pump on/off, connected to one of the usb ports, which will be turned on/off for this function.
-DHT11 Breakout Module: A sensor on a breakout board that is supposed to measure the humidity and temperature in the air outdoors. It's supposed to be displayed on the webpage as a stat and be available for controll of the pump inside the webpage
-Analog Hygrometer: Will be positioned in the soil right next to the tree. Is supposed to measure moisture of the soil. Will also be integrated into the webpage, just like the DHT11 (Note: Still need a way to connect this thing to the raspi. Some sort of waterproof 3 wire cable or something)
-Raspberry Pi 3b+: Brains of the operation. Will handle both the code and the webpage at the same time. Will run the pump over one of its usb ports and the sensors over its IO pins



Project Goals (simplified):

1) Sensor data collection: The program will need to collect data from the DHT11 breakout module and analog hygrometer sensors.
2) User settings and profiles: The program will need to allow users to set customizable settings for when the pump should turn on based on sensor data, such as minimum ground moisture and outside temperature.
3) Pump control: The program will need to turn on/off the USB water pump connected to one of the Raspberry Pi's USB ports based on the sensor data and user settings.
4) Webpage development: The program will need to have a simple webpage that displays the sensor data, including outside temperature, humidity, soil moisture, and the current status of the water pump. The webpage should also allow users to set and save their settings and profiles for the pump control.
5) Security: The program should have some form of user authentication to restrict access to the webpage and its functions.
6) 
