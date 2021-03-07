# IoT on Google Cloud with BigQuery
This project has been developed by Dr Lara Suzuki :woman_technologist: [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/larasuzuki.svg?style=social&label=Follow%20%40larasuzuki)](https://twitter.com/larasuzuki) at Google Inc.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/lasuzuki/StrapDown.js/graphs/commit-activity)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
![Profile views](https://gpvc.arturio.dev/lasuzuki)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/lasuzuki/StrapDown.js/graphs/contributors/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/lasuzuki)

[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/lasuzuki/)

In this tutorial I will demonstrate how to connect a Raspberry Pi and Sensor Hat onto Google Cloud using cloud Pub/Sub, and get the data persisted in Big Query

## Introduction to Sense Hat
The Sense HAT, which is a fundamental part of the [Astro Pi](https://astro-pi.org/) mission, allows your Raspberry Pi to sense the world around it.

The Sense HAT has a set of environmental sensors for detecting the surrounding conditions; it can measure pressure, temperature, and humidity. 

## Detecting Ambient Conditions

### The Sense HAT has two sensors capable of reading the ambient temperature: 
- the **humidity sensor** via the command *get_temperature_from_humidity* or *get_temperature*
- the **pressure sensor** via the command *get_temperature_from_pressure*

### The Sense Hat captures humidity condition of the ambient
- the **humidity sensor** via the command *get_humidity*

### The Sense Hat detects movement

The Sense HAT has an **IMU** (**I**nertial **M**easurement **U**nit) chip which includes a set of sensors that detect movement:
- A **gyroscope** for detecting which way up the board is, i.e., measures momentum and rotation
- An **accelerometer** for detecting movement, i.e., measures acceleration forces and can be used to find the direction of gravity
- A **magnetometer** for detecting magnetic fields, i.e., measures the Earth's own magnetic field somewhat like a compass

## The International Space Station
According to the [European Space Agency] (http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf), the International Space Station maintains these conditions at the following levels:

- **Temperature:** 18.3-26.7 Celsius
- **Pressure:** 979-1027 millibars
- **Humidity:** around 60%

The moviment sensor **IMU** is quite important when you’re in space. Astronauts needs to always know which way they are pointing. If they do not know their orientation, they have a problem. An **IMU Sensor** like the one in the **Sense Hat** is used on all manned and unmanned spacecraft to track movements and understand orientation. Although the IMU Sensor in the Sense Hat is not as accurate as the one used in real missions, like Apollo mission, it is much smaller and a million times cheaper! It is quite fascinating to see the difference in size and the advancement of tecnology from the 70s's to 2015 technologies (the year Sense Hat was created). The IMU of Apollo 11 is shown below, and you can read more about it on [the Apollo primary guidance, navigation, and control system (PGNCS)](https://en.wikipedia.org/wiki/Apollo_PGNCS).





