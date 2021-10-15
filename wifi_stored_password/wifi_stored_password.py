# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:58:23 2020

@author: =GV=
"""

from datetime import datetime as dt
import subprocess as sp
import webbrowser as wb

try:
    wifis = [(ssid.split(':')[1][1:-1], password.strip().split(':')[1][1:]) for ssid in sp.check_output(['netsh','wlan', 'show', 'profiles']).decode('utf-8').split('\n') if 'All User Profile' in ssid for password in sp.check_output(['netsh', 'wlan', 'show', 'profile', ssid.split(':')[1][1:-1], 'key=clear']).decode('utf-8').split('\n') if 'Key Content' in password]
except IndexError:
    ssids = [line.split(':')[1][1:-1] for line in sp.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n') if 'All User Profile' in line]
    wifis = []
    for ssid in ssids:
        try:
            pw = [line.strip().split(':')[1][1:] for line in sp.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode('utf-8').split('\n') if 'Key Content' in line]
            wifis.append((ssid, pw[0]))
        except IndexError:
            wifis.append((ssid, ''))
date_tag = dt.strftime(dt.date(dt.now()), '%Y%m%d')
with open(f'WIFI_stored_{date_tag}.txt', 'w') as f:
    f.write('disclaimer: I am not responsible for how this program is used\n')
    for wifi in wifis:
        f.write(f'\nSSID: \t{wifi[0]}\n')
        f.write(f'PW: \t{wifi[1]}\n')
    f.write("\nEPSTEIN DIDN'T KILL HIMSELF!!!")
    f.write('\n\n\nthanks!! \nby: =GV=')

wb.open(f'WIFI_stored_{date_tag}.txt')
