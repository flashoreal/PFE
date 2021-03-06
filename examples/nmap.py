__author__ = 'besimaltnok'

import nmap
import sys

nm = nmap.PortScanner()

port_list = [21,22,25,139,3306, 1248]
host = sys.argv[1]
argument = '-n -T4 -O -sV -p '
print "Scanning host : %s " %host
print "\n"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "Port\tName\tState\tReason"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
try:

	for i in port_list:
		sc = nm.scan(hosts=host, arguments=argument + str(i))
	   	print "%s\t%s\t%s\t%s" %(i, nm[host]['tcp'][i]['name'] , nm[host]['tcp'][i]['state'], nm[host]['tcp'][i]['reason'])
except KeyboardInterrupt:
	print "\n"
	print "!Scanning Stop!"
	exit
except NameError:
	print "Stop!!!!"
	exit

print "\n"
print "Scanned System Type :  %s " %(sc['scan'][host]['osmatch'][0]['name'])
print "Start scanning      : %s " % (sc["nmap"]['scanstats']['timestr'])
print "Scan Time           : %s " % (sc["nmap"]['scanstats']['elapsed'])



# Aktif bilgisayar tespiti

import nmap
nm = nmap.PortScanner()

hostlist = ['ipler_buraya']
for h in hostlist:
   sc = nm.scan(h, '80', '-sV -O')
   state = sc['nmap']['scanstats']['uphosts']
   if state == '1':
      print h, " : Aktif  host :)"
   else:
      print h, " : Kapali host :("


# Aktif bilgisayarların mac tespiti


import nmap
nm = nmap.PortScanner()

hostlist = ['ipler_buraya']
for h in hostlist:
   sc = nm.scan(h, '80', '-sV -O')
   state = sc['nmap']['scanstats']['uphosts']
   if state == '1':
      mac = sc['scan']['addressses']['mac']
      print mac, " : ", h
      
      
      
      
# Aktif bilgisayarların işletim sistemi bilgisini elde etmek

import nmap
nm = nmap.PortScanner()

hostlist = ['ipler_buraya']
for h in hostlist:
   sc = nm.scan(h, '80', '-sV -O')
   state = sc['nmap']['scanstats']['uphosts']
   if state == '1':
      os  = sc['scan'][h]['osmatch'][1]['osclass'][0]['osfamily']
      mac = sc['scan']['addressses']['mac']
      print mac, " : ", h, " : ", os 
