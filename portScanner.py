# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:49:29 2022

@author: User
"""

import socket

target = input("enter the ip address to scan")
portrange = input("enter the port range")

lowport = int(portrange.split('-') [0])
highport = int(portrange.split('-') [1])

print("scanning host:" , target , "from port " ,lowport , "to port " , highport )

for port in range(lowport,highport):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    status = s.connect_ex((target , port))
    if (status == 0):
        print("port " , port , " open")
    else:
        print("port " , port , " closed")
    s.close()    