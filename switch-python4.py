#!/usr/bin/env python3

import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

f = open('switchesIPs.txt')

for line in f:
   print("Configuring Switch " + line)
   HOST = line
   tn = telnetlib.Telnet(HOST)

   tn.read_until(b"Username: ")
   tn.write(user.encode('ascii') + b"\n")
   if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

   tn.write(b"conf t\n")

   for n in range (2,151):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name VLAN_" + str(n).encode('ascii') + b"_Python\n")

   tn.write(b"end\n")
   tn.write(b"exit\n")
   print(tn.read_all().decode('ascii'))

f.close()