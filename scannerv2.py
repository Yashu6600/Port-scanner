import sys
import socket
from datetime import datetime

#defining target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print ("Invalid amount of arguments.")
    sys.exit()
    
print("-"*50)
print("Scanning Target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

if sys.argv=="about":
    print ("Made by team 1")
try:
    for port in range(55,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print ("Checking port {}".format(port))
        if result == 0:
            print ("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print ("\nExiting program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could't connect to server.")
    sys.exit()
