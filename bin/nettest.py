#!/usr/bin/env python3

# OpenAssistant 0.02
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# Internet Connection Test By Kendy Hikaru And Kendy Hikaru

# nettest.py - Internet Connection Test

import time
import urllib.request, urllib.parse, urllib.error

REMOTE_SERVER = "http://www.speech.cs.cmu.edu"

def is_connected():

  """If Connected Return True, Or Else False"""
  try:
    response=urllib.request.urlopen(REMOTE_SERVER,timeout=1)
    return True
  except urllib.error.URLError as e: pass
  return False

if is_connected():
  print("internet access is currently available")
else:
  print("we are offline")