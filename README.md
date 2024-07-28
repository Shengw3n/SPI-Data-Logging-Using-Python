# SPI Data Logging Using Python

## Introduction

The project involves designing and implementing an SPI data logging system using Python to log and visualize temperature data from a 1T-8051 based series MCU.

![IMG_0670](https://github.com/user-attachments/assets/9a0fa883-8bcc-4739-945e-eddf4f09264b)

<img width="624" alt="Screenshot 2024-02-06 at 9 56 09 PM" src="https://github.com/user-attachments/assets/a1b3ac85-ecc2-40c4-b9be-db53b05ae4ce">

## Project Features

- **Real-time Temperature Monitoring:** Capable of real-time Temperature monitoring and display.
- **SPI Communication:** Utilizes the SPI protocol to transmit data from a microcontroller to a computer.
- **Data Logging:** Logs data received from the microcontroller into a file for persistent storage.
- **Python Integration:** Processes and visualizes the logged data using Python libraries.

## Hardware Components

- **Microcontroller:** N76E003 microcontroller
- **SPI Interface:** Standard SPI interface setup with necessary connections
- **Temperature Sensor:** LM335 temperature sensor

## Software Description

### Microcontroller Code

The microcontroller is programmed in assembly to collect temperature data from the LM335 sensor and transmit it via the SPI interface.

### Python Code

The Python script reads the data from the SPI interface, logs it into a file, processes it for analysis, and visualizes it using the Python library matplotlib.
