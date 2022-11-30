import subprocess
import os

#note to new raspberry pis, check  new USB_devices, since SDA partitian will change (ie not just sda1)

def difference(L1, L2):
    conjoin = set(L1).union(set(L2)) #creates a union of the list
    different_set = set(L1).intersection(set(L2)) #finds where list is the same
    difference = (conjoin - different_set) #gets the difference in the list
    return str(difference)

accepted_list = subprocess.getoutput('lsusb') #gets list of usb devices currently connected
#print(accepted_list)  
# ^^^ .split('\n') can get names from array, meaning device can be named for UI purposes
USB_device_list = subprocess.getoutput('ls /dev/sda*').split() #On Linux, /dev gets the devices on computer,
#sda is in charge of USBports, meaning for each USB device it creates a new portion of the sda (ie sda1, ...)
#print(USB_device_list)

c = 0
while c < 1: #change to True after rough draft
    if subprocess.getoutput('lsusb') != accepted_list: #checks if new device is input
        new_device_list = subprocess.getoutput('ls /dev/sda*').split() #gets new sda list

        #USB_device_list = ['/dev/sda', '/dev/sda1', '/dev/sda2', '/dev/sda3']
        #new_device_list = ['/dev/sda', '/dev/sda1', '/dev/sda2', '/dev/sda3', '/dev/sda6']

        item = difference(USB_device_list, new_device_list) #calls helper function to get difference alone
        os.system("echo aiden10 | sudo -S eject %s" % item) #using a function on Linux called eject, 
        # can remove USBs... note: needs to be installed on Linux machine previous, or better method needs
        # to be found...
    c += 1

#Needs to be changed when USB is inserted: echoing password for sudo command to work, while statement,
#UI for desgin