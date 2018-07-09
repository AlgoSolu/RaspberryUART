# Raspberry Pi3 UART RS232 with TouchScreen

## Requierements
* Raspberry Pi https://www.raspberrypi.org/
* TouchScreen https://github.com/goodtft/LCD-show
* MAX232 https://en.wikipedia.org/wiki/MAX232

## Hardware
This project use an RS232 with max232 chip for converting data to TTL (TX, RX).
RS232 ---> max232 ---> RaspberryPi (TTL RX)
RS232 <--- max232 <--- RaspberryPi (TTL TX)
Touch Screen bought on amazon: Quimat 8,9 cm TFT LCD with GPIO extension.
* Ground: must be the same for RS232, max232 and the Raspberry Pi, otherwise data on RX will be corrupted.
* Max232 Vcc: 3.3 Volts

## Install
* Install python > 3.7.0 https://www.python.org
* ```pip3 install Pillow```
* ```pip3 install pyserial```

## Configuration
* Configuration file: ```nano constants.py```
* Screen resolution: CAE mode 9 800x600 60Hz 4:3
* Serial port: Enabled

## Distribution
* ```sh install.sh```
