import socket
import sys
import re

global s
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def opt1(target):
    port = [ 20,21,22,23,25,53,67,68,80,123,161,162,389,443]
    service_name = {20:'FTP Data',21:'FTP Connection',22:'SSH',23:'Telnet',25:'SMTP',53:'DNS',67:'DHCP UDP port',68:'DHCP Cilent port',80:'HTTP',123:'NTP',161:'SNMP',162:'SNMP',389:'LDAP',443:'HTTPS'}
    print("===========================")
    print("Target Ip: ",target)
    print("===========================")
    try:
        for i in range(0,len(port)):
            if (s.connect_ex((target,port[i]))) == 0:
                print(f" {port[i]}:{service_name[port[i]]} =====>  open")
            else:
                print(f" {port[i]}:{service_name[port[i]]} =====>  close")
        s.close()
    except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit()
    except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit()
    except socket.error: 
            print("\ Server not responding !!!!") 
            sys.exit()
            
def opt2(target):
    ip = socket.gethostbyname(target)
    print("===========================")
    print("Target Ip: ",ip)
    print("===========================")
    try:
        for port in range(1,65535):
            if (s.connect_ex((ip,port))) == 0:
                print(f" port{port}  =====>  open")
        s.close()
    except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit()
    except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit()
    except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit()
     
def main():
    x = ''
    target = input("Enter Target Hostname or IP Address:\t")
    x = re.findall("[0-9]",target)
    if x:
        pass
    else:
        target = socket.gethostbyname(target)
    try:
        opt = int(input("Which Opterationn want to perform:\n1:Comman Ports\n2:All Ports\nEnter the choice:\t"))
        if (opt == 1):
            opt1(target)
        elif (opt == 2):
            opt2(target)
        elif (opt >= 3 or opt <= 0 ):
            print("ENter Correct Operations!!")
            sys.exit()
    except ValueError:
        print("Enter the correct Operation not any string!!!")
        sys.exit()
        
if __name__ == '__main__' :
    try:    
        main()
    except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit()
        
