import os
import time 

REPEAT_INTERVAL = 3600 # Repeat frequency in seconds

while True:
  command = "osascript -e \'say \"Hey Ali drink water\"\'; osascript -e \'display alert \"Hey Ali, Drink water\"\'"
  os.system(command)
  time.sleep(REPEAT_INTERVAL)