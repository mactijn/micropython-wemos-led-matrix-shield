# Wemos D1 Mini Matrix LED shield driver for micropython

## Introduction
This is an implementation of the driver for the Wemos D1 Mini
Matrix LED shield, which utilizes the TM1640 chip by Titan Micro.

It implements a weird protocol, which reminds both of I2C and SPI
but is not compatible with either. This is why we bitbang.

This code has been optimized for use with the Matrix LED
shield by Wemos. It has been tested on a Wemos D1 Mini and
an MH-ET Live MiniKit, using micropython 1.9.2.

Protocol implementation was derived from Wemos'
[own implementation](https://github.com/wemos/WEMOS_Matrix_LED_Shield_Arduino_Library/) of the driver for Arduino.

## Functionality
- Modify the state of individual pixels
- draw an 8x8 bitmap
- set the brightness

### Animations
Animation functions are in a separate class. These will allow
you to define a simple multi-frame animation.

## Usage
Please see `example.py` for example usage.
