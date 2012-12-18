#!/usr/bin/python

import subprocess

def shine(r, g, b):
  """Make blink(1) shine in the given color."""
  subprocess.call(['blink1-tool', '--rgb', ','.join(map(str, [r, g, b]))])

def off():
  """Turn off the blink(1)."""
  subprocess.call(['blink1-tool', '--off'])
