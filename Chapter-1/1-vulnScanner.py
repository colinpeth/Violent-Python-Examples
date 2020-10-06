#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import os
import sys

#Connects to socket and trys to get banner
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

#Checkes for vulnerabilities 
def checkVulns(banner, filename):
    #Opens file and reads lines.
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+] Server is vulnerable: ' +\
                banner.strip('\n')


def main():
    #Checks System arguments for filename
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        
        #Checks if file exists
        if not os.path.isfile(filename):
            print '[-] ' + filename +\
                ' does not exist.'
            exit(0)
        #Checkes if access is allowed file
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename +\
                ' access denied.'
            exit(0)
    else:   
        print '[-] Usage: ' + str(sys.argv[0]) +\
            ' <vuln filename>'
        exit(0)

    #Runs port scanning to see if ip is available 
    portList = [21,22,25,80,110,443]
    #Loops through IP addressed
    for x in range(147, 150):
        ip = '192.168.95.' + str(x) #Adds ending of IP
        #Loops through port lisr
        for port in portList:
            banner = retBanner(ip, port)
            #Prints Banner if avaibale
            if banner:
                print '[+] ' + ip + ' : ' + banner
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()
