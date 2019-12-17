#!/usr/bin/env python3

# Import of python system library.
# This library is used to download the 'index.html' from server.
# You don't have to install anything special, this library is installed with Python.
import urllib.request, time, sys

def my_connect():
    fp = urllib.request.urlopen("http://server:1234/", None, 5)

    encodedContent = fp.read()
    decodedContent = encodedContent.decode("utf8")
    print(decodedContent)
    fp.close()

while True:
    try:
        my_connect()
    except:
        print("Something went wrong")
    sys.stdout.flush()
    time.sleep(20)
