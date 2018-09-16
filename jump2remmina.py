#!/usr/bin/python

# File converts from JumpDesktop format to Remmina.
# group part is just what I need
# copyleft by paczor@fubar.pl

import json

# ColorDepthCode    integer	the remote display's colour depth. 0 - 8 bit colour depth, 2 - 16 bit colour depth, 3 - 24 bit colour depth, 4 - black and white (VNC only), 5 - gray scale (VNC only)
def colorDepth(inDepth):
    outDepth = ""
    if inDepth == 0:
	outDepth = "8"
    elif inDepth == 2:
	outDepth = "16"
    elif inDepth == 3:
	outDepth = "24"
    elif inDepth == 4:
	outDepth = ""
    elif inDepth == 5:
	outDepth = ""
    else:
	outDepth = ""
    return outDepth

# This is only for myself ;)
def printGroup(inGroup):
    outGroup = "" 
    if "BAGNO2" in inGroup:
	outGroup = "BAGNO2"
    elif "BAGNO" in inGroup:
	outGroup = "BAGNO"
    elif "DOM" in inGroup:
	outGroup = "DOM"
    elif "NOBLE" in inGroup:
	outGroup = "NOBLE"
    elif "PRZAS" in inGroup:
	outGroup = "PRZASNYSKA"
    elif "ZAKO" in inGroup:
	outGroup = "ZAKOPANE"
    elif "ZWIR" in inGroup:
	outGroup = "ZWIRKI"
    else:
	outGroup = "INNI"
    return outGroup
	

def outputRemmina(pj):
    print "[remmina]"
    if pj['ClipboardRedirection'] == True:
	print "disableclipboard=0"
    else:
	print "disableclipboard=1"
    print "ssh_auth=0"
    print "clientname="

#REMMINA:   Quality 2 means "Good", no direct equivalent in JumpDesktop
    print "quality=2"
    print "ssh_charset="
    print "ssh_privatekey="
    print "sharesmartcard=0"

#JUMPDSK:  MatchScreenResolution boolean set to true match the local monitor's resolution 
#JUMPDSK:  this makes Jump ignore the ResolutionWidth and ResolutionHeight fields
#REMMINA:  Empty "Use client resolution"
    print "resolution=%sx%s" % (pj['ResolutionWidth'], pj['ResolutionHeight'])

    print "group=%s" % printGroup(pj['DisplayName'])
    print "password="
    print "name=%s" % pj['DisplayName']
    print "ssh_loopback=0"
    if pj['RdpPrinterRedirection'] == True:
	print "shareprinter=1"
    else:
	print "shareprinter=0"
    print "ssh_username="
    print "ssh_server="
    print "security="
    print "protocol=RDP"
    print "execpath="

# AudioPlaybackCode   integer	Controls how audio is redirected. 
# 0 - don't play audio, 
# 1 - play on remote server, 
# 2 - play on local device. This is RDP only.
    print "sound=off"

    print "exec="
    print "ssh_enabled=0"
    print "username=%s" % pj['Username']

#JUMPDSK:	DriveMappings array of drive mappings RDP only. 
#JUMPDSK:	Each element in the array is a dictionary.
#JUMPDSK:	Drive mapping format keys
#JUMPDSK:	Key Type    Description
#JUMPDSK:	DisplayName	string	the display name to show in the UI for the drive mapping
#JUMPDSK:	Enabled	    boolean	true if the mapping is enabled, false otherwise
#JUMPDSK:	IsReadOnly  boolean	true if the mapping is read only and can not be written to by the remote computer
#JUMPDSK:	LocalPath   string  the local path to map
#JUMPDSK:	UniqueId    string  unique id for this drive mapping
#JUMPDSK:	
#JUMPDSK:	Example with one drive mapping:
#JUMPDSK:	
#JUMPDSK:	  "DriveMappings": [
#JUMPDSK:	    {
#JUMPDSK:	      "DisplayName": "Downloads",
#JUMPDSK:	      "Enabled": true,
#JUMPDSK:	      "IsReadOnly": false,
#JUMPDSK:	      "LocalPath": "/Users/me/Downloads",
#JUMPDSK:	      "UniqueId": "11A92900-35A4-412C-983D-EE276A2A824F"
#JUMPDSK:	    }
#JUMPDSK:	  ],
    print "sharefolder="

    print "console=0"
    if pj['Domain'] != 'null': print "domain=%s" % pj['Domain'] 
    print "server=%s" % pj['TcpHostName']
    print "colordepth=%s" % colorDepth(pj['ColorDepthCode'])
    print "window_maximize=0"
    print "window_height=1800"
    print "window_width=2880"
    print "viewmode=1"

# parse JumpDesktop file
def parseFile(plik):
    with open(plik, 'r') as myfile:
	json_string = myfile.read()
	pj = json.loads(json_string)
	outputRemmina(pj)


def check_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} not exists".format(x))
    return x

if __name__ == "__main__":
    import argparse, sys, os, re
    from argparse import ArgumentParser
    parser = ArgumentParser(description="JumpDesktop to Remmina converter")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=check_file,
        help="input Jump file ", metavar="FILE")
    args = parser.parse_args()

    inputfile = args.filename
    parseFile(inputfile)
