import sys
import operator
import requests
import json

kanyeCDString = ""
kanyeCDFile = open("rappers/kanye/CollegeDropout_R.txt", "r")
kanyeCDString = kanyeCDFile.read()

thing = 1
while thing:
    print (kanyeCDString)
