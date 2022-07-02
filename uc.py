import os
import sys
import time
os.system('clear')
try:
    from googlesearch import search
except ImportError: 
    print(bcolors.udpx + "No module named 'google' found" + bcolors.ucp)
from colorama import init
init()

class bcolors:
    HEADER = '\033[95m'
    blue = '\033[94m'
    ucts = '\033[96m'
    green = '\033[92m'
    mlms = '\033[93m'
    udpx = '\033[91m'
    ucp = '\033[0m'
    mex = '\033[1m'
    tts = '\033[4m'

def paradoxlogo():
	print(bcolors.HEADER + """
      ___           ___     
     /\  \         /\__\    
     \:\  \       /:/  /    
      \:\  \     /:/  /     
  ___  \:\  \   /:/  /  ___ 
 /\  \  \:\__\ /:/__/  /\__\
 \:\  \ /:/  / \:\  \ /:/  /
  \:\  /:/  /   \:\  /:/  / 
   \:\/:/  /     \:\/:/  /  
    \::/  /       \::/  /   
     \/__/         \/__/    
 
Url collector by Mr. Onion    
Telegram: https://t.me/mronion420
Facebook: https://www.facebook.com/mr.x3n0n

""" + bcolors.green + """

Example:- python2 uc.py -d "Dork" url_number -s listname.txt

Show usage: python2 uc.py -h

""" + bcolors.ucp)

def PrU(dork,weo_numb,enable_save,filename):

	print (bcolors.tts + "Start Collecting Urls... \n" + bcolors.ucp)
	
	pages = 0
	
	try:
		for qwdw in search(dork, tld="com", lang="es", num=weo_numb, start=0, stop=None, pause=2):
			print ("[+] " + bcolors.green + qwdw + bcolors.ucp)
			time.sleep(0.2)
			
			pages += 1
			
			if pages >= weo_numb:
				break
			
			data = (qwdw)
			
			if enable_save == 1:
				file = open(filename, "a")
				file.write(str(data))
				file.write("\n")
				file.close()
				
	except HTTPError:
		if e.code == 429:
		     print (bcolors.udpx + " Too Many Requests\n" + bcolors.ucp)
		     print ("Loading...")


def prmain():
	paradoxlogo()
	enable_save = 0
	filename = ""

	if len(sys.argv) == 1:
		print (bcolors.udpx + "FINISHED" + bcolors.ucp)
	elif len(sys.argv) == 2:
		arg = sys.argv[1]
		
		if arg == "-h" or arg == "--help" :
			print ("HELP SECTION:\n")
			print ("Usage: \tpython2 uc.py dork number of websites u want \n")
			print ("Example: \tpython2 uc.py inurl:admin 20 -s listname.txt \n")
			print ("-d,--dork \tSpecifies the dork to use in the tool")
			
			print ("-v,--version \tShow version")
			print ("-s,--save \tEnable save List of websites in txt file")
		elif arg == "-v" or arg == "--version":
			print ("url collector By Mr Onion 420")
		else:
			print (bcolors.udpx + "ERROR: Incorrect argument or sintaxis" + bcolors.ucp)
			
	elif len(sys.argv) > 2 and len(sys.argv) <= 6:

		if sys.argv[1] == "-d" or sys.argv[1] == "--dork":
			
			dork = sys.argv[2]
			weo_numb = int(sys.argv[3])
			
			if(len(sys.argv) > 4):
				if sys.argv[4] == "-s" or sys.argv[4] == "--save":
					enable_save = 1
					filename = sys.argv[5]

			PrU(dork,weo_numb,enable_save,filename)
				
prmain()