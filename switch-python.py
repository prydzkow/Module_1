import getpass
import telnetlib

HOST = "192.168.122.12"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name VLAN_2_Python\n")
tn.write(b"exit\n")
tn.write(b"vlan 3\n")
tn.write(b"name VLAN_3_Python\n")
tn.write(b"exit\n")
tn.write(b"vlan 4\n")
tn.write(b"name VLAN_4_Python\n")
tn.write(b"exit\n")
tn.write(b"vlan 5\n")
tn.write(b"name VLAN_5_Python\n")
tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
