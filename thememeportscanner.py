#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

print "#" * 23                                                                                       
print "# Brians port scanner #"
print "#" * 23

print "dankmemescantmeltsteelbeamsdankmemescantmeltsteelbeamssoinhalethememes"

# Ask for input
remoteServer    = raw_input("Please enter an IP in your network to scan the memez ;): ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# super duper legitnez banner
print "memez" * 15
print "Scanning remote host, harambe says wait, this may take a while ", remoteServerIP
print "memez" * 15

# start time check B)
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:      Open".format(port)
        sock.close()

#some error handling for catching errors

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
