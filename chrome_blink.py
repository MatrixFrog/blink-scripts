#!/usr/bin/python

import blink
import time
import urllib2

def getTreeStatus():
  """Fetches the Chrome tree status."""
  url = 'http://chromium-status.appspot.com/status'
  status = urllib2.urlopen(url).read().lower()
  if 'closed' in status or status == '0':
    return 'closed'
  elif 'open' in status or status == '1':
    return 'open'
  return 'unknown'

def showTreeStatus():
  status = getTreeStatus()
  if status == 'open':
    blink.shine(0x00, 0xff, 0x00)
  elif status == 'closed':
    blink.shine(0xff, 0x00, 0x00)
  else:
    blink.shine(0xff, 0xff, 0x00)

def main():
  try:
    while True:
      showTreeStatus()
      time.sleep(60)
  except KeyboardInterrupt:
    blink.off()

if __name__ == '__main__':
  main()
