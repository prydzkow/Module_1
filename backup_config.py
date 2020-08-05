#!/usr/bin/env python3

import getpass
import telnetlib

#Getting username and password
user = input("Enter your username: ")
password = getpass.getpass()

#Opening txt file with IPs of the switches
f = open('switchesIPs.txt')

#Getting running config from the switches
for line in f:
   print("Backing up Switch Configuration " + line)
   HOST = line.strip()
   tn = telnetlib.Telnet(HOST)

   tn.read_until(b"Username: ")
   tn.write(user.encode('ascii') + b"\n")
   if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

   tn.write(b"wr\n")
   tn.write(b"terminal length 0\n")
   tn.write(b"sh run\n")
   tn.write(b"exit\n")
   readoutput = tn.read_all().decode('ascii')
   saveoutput = open("switch-" + HOST + ".bk", "w")
   saveoutput.write(readoutput)
   saveoutput.write("\n")
   saveoutput.close
   print(tn.read_all().decode('ascii'))