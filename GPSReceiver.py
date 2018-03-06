#!/usr/bin/env python3
# coding=utf-8

import sys
from datetime import datetime
from math import modf
from time import sleep
from gps3 import misc


from gps3 import gps3
gps_socket = gps3.GPSDSocket()
gps_socket.connect()
gps_socket.watch()

data = gps3.DataStream()

file = open('./GPS.data',mode='a')

for new_data in gps_socket:
    if new_data:
        data.unpack(new_data)

        alt = data.TPV['alt']
        lat = data.TPV['lat']
        time_current = 'Time:  {time} '.format(**data.TPV)

        data_str = time_current +',\t' + 'Altitude = '+str(alt) + ',\tLatitude' + str(lat)

        file.writelines(data_str+'\n')

        print(time_current)
        print('Altitude = ',data.TPV['alt'])
        print('Latitude = ',data.TPV['lat'])
        print()
