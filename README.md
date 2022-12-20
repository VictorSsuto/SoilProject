# SoilProject
### This project is done in the scope of the iOT class (420-N55-LA) at Champlain College Regional 

Soil project aims to help users determinating the **ammount of light** their plants are getting and the **humidity index** of their plants while using **arduino sensors** and **device**. These devices are tied to a **python** environment which allows to view the information gatthered by the front end with **aggregation/pipeline** and **time series collection**. The information is then stored in **MongoDB**.

# Target audience: 

This project aims to please anyone that want to take care of their plants while using the Internet of Things (iOT). 

# Hardware design 

  - Sensors Used
      - [Arduino Soil Moisture Sensor](https://m.media-amazon.com/images/I/51viGBnJOhL._AC_.jpg)
      - [Photoresistor](https://en.wikipedia.org/wiki/File:LDR_1480405_6_7_HDR_Enhancer_1.jpg)
      - [ArduinoMKR1010](https://docs.arduino.cc/static/df779d958c386826c73e149e42e28918/image.svg)


      
  - [Hardware Schematics](https://user-images.githubusercontent.com/83074897/208696296-8e76aa25-d190-4d38-9ced-4eff7b94b525.png)
  - Data sampling 
    - Humidity%
    - Light: resuistance(ohms)/lux


# Mongo db schema design 
  - [Sensor data sampling and specifications for humidty](https://user-images.githubusercontent.com/83074897/208696590-4d9b1339-91c2-4ae4-9613-356ba2b938d7.png)
  - [Sensor data sampling and specifications for Light](https://user-images.githubusercontent.com/83074897/208696765-c87451fb-7474-436f-b79e-d474f785d547.png)


# Api method with expected response: 


