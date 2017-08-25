import json;
import urllib;
import math;
import sys;
import requests;
import time;
   
placeName = raw_input("Please enter the name of the place you wish to look up: ");

# Set the default URL to be visited
MAIN_URL = "http://maps.googleapis.com/maps/api/geocode/json?";

def getCurrentLocation():
    '''
    This function operates every 30 seconds and connects to a free API to rettrieve your current location
    This means that the device that the program will run in can be used in a mobile object such as a car
    :return: a tuple: the current latitude and longitude
    '''

    send_url = 'https://freegeoip.net/json';
    requesting = requests.get(send_url);
    currentLocJson = json.loads(requesting.text);
    currentLat = currentLocJson['latitude'];
    currentLon = currentLocJson['longitude'];
    time.sleep(5);
    return currentLat, currentLon;

def dirInDegs(slat , slon , elat , elon):# The calc function
    radians = math.atan2((elon-slon),(elat-slat));
    compassReading = radians * (180 / math.pi);
    return compassReading;


def getLatLon(address):
    # Mostly your business code
    raw_data = str(urllib.urlopen(MAIN_URL + urllib.urlencode({"sensor":"false", "address": address})).read());
    json_data = json.loads(raw_data);
    lat = json_data["results"][0]["geometry"]["location"].values()[0];
    lon = json_data["results"][0]["geometry"]["location"].values()[1];
    return lat, lon; # Returns tuple

while True:
    if len(placeName) < 1: sys.exit([1]);
    print "Retrieving coordinates of current location...";
    curr_lat, curr_lon = getCurrentLocation();
    print "Retrieving coordinates of entered location...";
    loc_lat, loc_lon = getLatLon(placeName);
    print dirInDegs(curr_lat, curr_lon, loc_lat, loc_lon);
