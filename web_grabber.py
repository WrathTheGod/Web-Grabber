import urllib
import httplib
import socket

print "\n\nFast Webpage Saver"
print "Input URL and Run it, It will save the Webpage within seconds"



try:
	url = raw_input("URL:")
	url = url.replace("http://","")
	txt = open('savedpage.html','w')
	cobra = urllib.urlopen('http://'+url)
	for source in cobra.readlines():
		print source.rstrip()
		txt.write(source.rstrip())
	txt.close()
	cobra.close()
raw_input('Complete: Open savedpage.html')
except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\t[x] Session cancelled"
