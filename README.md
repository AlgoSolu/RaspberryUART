# Raspberry Pi3 UART with TouchScreen

## Hardware configuration
This project use an RS232 with max232 chip for converting data to TTL (TX, RX).
RS232 ---> max232 ---> RaspberryPi (TTL RX)
RS232 <--- max232 <--- RaspberryPi (TTL TX)
Touch Screen was bought on amazon: Quimat 8,9 cm TFT LCD with GPIO extension.
Note: The GND must be the same for RS232, max232 and the Raspberry Pi, otherwise data on RX will be corrupted.

## Install
* Install python > 3.7.0 https://www.python.org
* pip3.7 install Pillow
* pip3.7 install pyserial

## Configuration
* Configuration file: constants.py
