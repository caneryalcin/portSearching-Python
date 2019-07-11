import sys
import subprocess
from  socket import *
from  datetime import  datetime
import subprocess as sp

sp.call('clear',shell=True)

s = socket(AF_INET,SOCK_STREAM)
server = input("Host adress: ")

print ("-" * 60)
print ("Please wait, scanning host")
print ("-" * 60)

#Check what time the scan started
time1 = datetime.now()

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False


try:
    for port in range(1, 40):
        if pscan(port):
            print("Port ", port, "is open")
        else:
            print("Port ", port, "is closed")
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
time2 = datetime.now()

# Calculate amount of time searching for ports
total = time1 - time2
print("Scanning completed in: ", total)


