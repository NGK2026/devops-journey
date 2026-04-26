# https://autbor.com/simplecountdown.py - A simple countdown script

import time, subprocess

time_left = 10

try:
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left = time_left - 1

    # at end of countdown, play sound file:
    # subprocess.run(['xdg-open', 'alarm.wav'])
    # or use mpv and set to loop infinity!!!
    # subprocess.run(['mpv', '--loop=inf', 'alarm.wav'])
    # or use mpv --really-quiet muhahah
    subprocess.run(['mpv', '--loop=inf', '--really-quiet', 'alarm.wav'])
except KeyboardInterrupt:
    print("\n[!] cancelled by user.")