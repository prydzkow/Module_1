#!/usr/bin/env python3

import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

for n in range(13, 17):
   HOST = b"192.168.122." + str(n).encode('ascii')
   tn = telnetlib.Telnet(HOST)

   tn.read_until(b"Username: ")
   tn.write(user.encode('ascii') + b"\n")
   if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

   tn.write(b"conf t\n")

   for n in range (2,21):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name VLAN_" + str(n).encode('ascii') + b"_Python\n")

   tn.write(b"end\n")
   tn.write(b"exit\n")
   print(tn.read_all().decode('ascii'))