#!/usr/bin/env python3

# nettest.py - Internet Connection Test

import time
import urllib.request, urllib.parse, urllib.error

REMOTE_SERVER = "https://weblife.org"

def is_connected():

  """If Connected Return True, Or Else False"""
  try:
    response=urllib.request.urlopen(REMOTE_SERVER,timeout=1)
    return True
  except urllib.error.URLError as e: pass
  return False

if is_connected():
  print("Internet access is currently available.")
else:
  print("We are offline.")