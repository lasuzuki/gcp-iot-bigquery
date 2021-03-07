# IoT on Google Cloud with BigQuery
This project has been developed by Dr Lara Suzuki :woman_technologist: [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/larasuzuki.svg?style=social&label=Follow%20%40larasuzuki)](https://twitter.com/larasuzuki) and supervised by Vint Cerf :technologist: [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/vgcerf.svg?style=social&label=Follow%20%40vgcerf)](https://twitter.com/vgcerf), both at Google Inc.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/lasuzuki/StrapDown.js/graphs/commit-activity)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
![Profile views](https://gpvc.arturio.dev/lasuzuki)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/lasuzuki/StrapDown.js/graphs/contributors/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/lasuzuki)

[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/lasuzuki/)

In this tutorial I will demonstrate how to connect a Raspberry Pi and Sensor Hat onto Google Cloud using cloud Pub/Sub, and get the data persisted in Big Query

# Introduction to Sense Hat
The Sense HAT, which is a fundamental part of the [Astro Pi](https://astro-pi.org/) mission, allows your Raspberry Pi to sense the world around it.

The Sense HAT has a set of environmental sensors for detecting the surrounding conditions; it can measure pressure, temperature, and humidity. 

## Detecting Ambient Conditions

1. The Sense HAT has two sensors capable of reading the ambient temperature: 
- the **humidity sensor** via the command *get_temperature_from_humidity* or *get_temperature*
- the **pressure sensor** via the command *get_temperature_from_pressure*

2. The Sense Hat captures humidity condition of the ambient
- the **humidity sensor** via the command *get_humidity*

3. The Sense Hat detects movement

The Sense HAT has an **IMU** (**I**nertial **M**easurement **U**nit) chip which includes a set of sensors that detect movement:
- A **gyroscope** for detecting which way up the board is, i.e., measures momentum and rotation
- An **accelerometer** for detecting movement, i.e., measures acceleration forces and can be used to find the direction of gravity
- A **magnetometer** for detecting magnetic fields, i.e., measures the Earth's own magnetic field somewhat like a compass

The Earth rotates around an axis that runs between the North and South Poles. All objects have three axes around which they can rotate. If you know how much rotation has happened on each axis of an object, then you know which way the object is pointing. The axis are:

- Pitch
- Roll 
- Yaw

To get the an object into a specific position, you can rotate it by a known amount around each of the three axes. The image below shows where the three axes are in relation to the Sense HAT.

<img src="https://github.com/lasuzuki/gcp-iot-bigquery/blob/main/blob/rotation_movement.jpg" width=400 align=center>

The **get_accelerometer_raw()** method tells you the amount of G-force acting on each axis (x, y, z). If any axis has ±1G, then you know that axis is pointing downwards. If the board is only rotated, it will only ever experience 1G of acceleration in any direction; if we were to shake it, the sensor would experience more than 1G. We could then detect that rapid motion and respond.

# The International Space Station
According to the [European Space Agency] (http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf), the International Space Station maintains these conditions at the following levels:

- **Temperature:** 18.3-26.7 Celsius
- **Pressure:** 979-1027 millibars
- **Humidity:** around 60%

The moviment sensor **IMU** is quite important when you’re in space. Astronauts needs to always know which way they are pointing. If they do not know their orientation, they have a problem. An **IMU Sensor** like the one in the **Sense Hat** is used on all manned and unmanned spacecraft to track movements and understand orientation. Although the IMU Sensor in the Sense Hat is not as accurate as the one used in real missions, like Apollo mission, it is much smaller and a million times cheaper! It is quite fascinating to see the difference in size and the advancement of tecnology from the 70s's to 2015 technologies (the year Sense Hat was created). The IMU of Apollo 11 is shown below, and you can read more about it on [the Apollo primary guidance, navigation, and control system (PGNCS)](https://en.wikipedia.org/wiki/Apollo_PGNCS).

<img src="https://github.com/lasuzuki/gcp-iot-bigquery/blob/main/blob/appolo%2011.jpg" width=400 align=center>

# Collecting data from Sense Hat using Google Cloud Platform Pub Sub

You can find how to connect your Raspberry Pi and Sense Hat to Google Cloud Pub sub by following the tutorial [Telemetry Data on Google Cloud using Pub/Sub, IoT Core and DTN] https://github.com/lasuzuki/dtn-gcp-iot. 

In this tutorial we will be using a function **iot.py** that besides sharing data using DTN we persist information into Google Cloud BigQuery

## Google Cloud Big Query
Big Data require expensive servers and skilled database administrators, and managing data centers and tuning software takes time & money. Even MapReduce based analysis can be slow for ad-hoc queries. Google BigQuert deliver Analytics as a service. Gigabyte- to petabyte-scale storage and SQL queries, BigQuery is Encrypted, durable, and highly available. It is fully managed and serverless for maximum agility and scale. It has also built-in ML for out-of-the-box predictive insights, and high-speed, in-memory BI Engine for faster reporting and analysis.

In this tutorial we will be persisting data collected from Sense Hat to BigQuery for further analysis and reporting, and even the use of BigQueryML to build machine learning on top of the data we collect from the environment.

The file **iot.py** contains the code that we receive in pub/sub via mqtt using Paho broker in our Raspberry Pi. 

