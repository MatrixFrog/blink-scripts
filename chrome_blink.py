#!/usr/bin/python

import subprocess
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
    shine(0x00, 0xff, 0x00)
  elif status == 'closed':
    shine(0xff, 0x00, 0x00)
  else:
    shine(0xff, 0xff, 0x00)

def shine(r, g, b):
  """Make blink(1) shine in the given color."""
  subprocess.call(['blink1-tool', '--rgb', ','.join(map(str, [r, g, b]))])

def off():
  subprocess.call(['blink1-tool', '--off'])

def main():
  try:
    while True:
      showTreeStatus()
      time.sleep(60)
  except KeyboardInterrupt:
    off()

if __name__ == '__main__':
  main()
