#!/usr/bin/python

"""Shows the status of a laptop battery on a blink(1).
   Green for 100%, red for 0%, and somewhere in between for partially charged.

   Uses 'acpi': sudo apt-get install acpi
"""

from __future__ import division
import blink
import re
import subprocess
import time


def showBatteryStatus():
  batteryInfo = subprocess.check_output(['acpi', '--battery'])
  batteryPercentage = int(re.search(r'(\d+)%', batteryInfo).group(1))
  assert 0 <= batteryPercentage <= 100
  showPercentage(batteryPercentage)
  
def showPercentage(batteryPercentage):
  print 'Battery is at %s%%' % batteryPercentage
  batteryFraction = batteryPercentage / 100
  blink.shine(0xff * (1 - batteryFraction), 0xff * batteryFraction, 0x00)
 
def main():
  try:
    while True: 
      showBatteryStatus()
      time.sleep(30)
  except KeyboardInterrupt:
    blink.off() 

if __name__ == '__main__':
  main()

