# WUtoWXnow
A simple python script to take personal weather station that is uploaded to WeatherUnderground and have it output to a WXnow.txt file for APRS use
I created this becasue I was unable to get WeeWX working correctly on my RPi1A and did not like the solutions using an SDR to pull the data OTA.

This script generates a WXnow.txt file in the 2 line Cumulus format.

You must add your Station ID and API key to the WUtoWXnow.py file for this work work correctly.

Script updates the WXnow.txt file once every 60 seconds and is in the format used my most common APRS clients.

Note this script was designed to pull data from WU that was being uploaded from my Accurite Atlas PWS, results with other PWS my vary. That being said it SHOULD work with other PWS that upload to WeatherUnderground such as the Tempest Weather System.
