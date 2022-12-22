# Soil Project
### This project is done in the scope of the iOT class (420-N55-LA) at Champlain College Regional 

Soil project aims to help users determinating the **ammount of light** their plants are getting and the **humidity index** of their plants while using **arduino sensors** and **device**. These devices are tied to a **python** environment which allows to view the information gatthered by the front end with **aggregation/pipeline** and **time series collection**. The information is then stored in **MongoDB**.

# Target audience: 

This project aims to please anyone that want to take care of their plants while using the Internet of Things (iOT). 

# Hardware design 

  - Sensors Used
      - [Arduino Soil Moisture Sensor](https://m.media-amazon.com/images/I/51viGBnJOhL._AC_.jpg)
      - [Photoresistor](https://en.wikipedia.org/wiki/File:LDR_1480405_6_7_HDR_Enhancer_1.jpg)
      - [ArduinoMKR1010](https://docs.arduino.cc/static/df779d958c386826c73e149e42e28918/image.svg)


      
  - [Hardware Schematics](https://user-images.githubusercontent.com/83074897/209220588-29fc6c4f-e29d-49ad-85c4-aa6946a155fa.png)
    - Black wire -> Ground
    - Red wire -> 5v
    - Yellow wire -> Analogue 0
  - Data sampling 
    - Humidity%
    - Light: resuistance(ohms)/lux


# Mongo db schema design 
  - [Sensor data sampling and specifications for humidty](https://user-images.githubusercontent.com/83074897/208696590-4d9b1339-91c2-4ae4-9613-356ba2b938d7.png)
  - [Sensor data sampling and specifications for Light](https://user-images.githubusercontent.com/83074897/208696765-c87451fb-7474-436f-b79e-d474f785d547.png)


# Api method with expected response: 

GET -/devices

Description 

This method reads the data from our emulated data. 

HTTP response status code

400 - Bad Request

200 - Ok

500 - Internal Server Error

------------------------------------------------------

GET -/devices/<int:deviceId>

Description 

This method reads the data from our emulated data. It can categorize it by an ID and it returns the average Humidity and Lumens. 

HTTP response status code

400 - Bad Request

200 - Ok

500 - Internal Server Error

------------------------------------------------------

 
POST -/device/<int:device>/devices

Description

This methods creates data. It was used as a test at first. It is now not needed.

HTTP response status code

400 - Bad Request

200 - Ok

500 - Internal Server Error















