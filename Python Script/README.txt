
Homework 6
CS 453
John Miller


++++++++++++++++++++++
+     BACKGROUND     +
++++++++++++++++++++++

I am working with a team for EE300 (Cornerstone). We built an IOT Arduino based soil temperature sensor that sends hourly temperature data to Google Sheets. The data will then be used to send automated Tweets or text messages to subscribers informing them when it is safe to plant certain crops. The scope of the project is the hardware and software for the sensor, but not the data collected. The only analysis we are performing is in the way of a graph in Google Sheets. In essence, the data is being collected, but nothing is actually being done with the data yet. The client will need to design his own system for automating the alerts.

++++++++++++++++++++++++
+     WHAT IT DOES     +
++++++++++++++++++++++++

This program takes the temperature data from two sensors and makes makes dictionaries of of each device and nested dictionary containing the daily averages. Another dictionary is created that contains the devices and a nested dictionary of crops with the value that says it is safe to plant. Since the alert service is yet to be determined, a print statement is at the end.

++++++++++++++++++++++
+       FILES        +
++++++++++++++++++++++

Program : SoilTemp.py
Input file : DataCollector - DataLogger.csv
Output : Daily Averages.png
Raw Data Report from Google Sheets: DataCollector - Summary.pdf



++++++++++++++++++++++
+ NOTES AND CAVEATS  +
++++++++++++++++++++++

    * Most of the data collected for this assignment is from a breadboarded device in my window.
    * The final device that we built sent some data, but due to sensor wiring problems, it sent the max value.
    * The data is not an actual temperature, it is the raw sensor output. It is, however proportional to the temperature.
    * The "temperature" readings are from air, rather than soil temperature. This means there is a wide range of readings.


