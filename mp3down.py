  1 #Music Downloader
  2 #Made by : Anubhav Srivastava
  3 # @IIIT Hyderabad
  4 pr=[]
  5 
  6 import urllib2
  7 import re
  8 
  9 from bs4 import BeautifulSoup
 10 name=raw_input()
 11 response=urllib2.urlopen("http://www.emp3world.com/search/%s_mp3_download.html" %(name))
 12 html=response.read()
 13 #soup=BeautifulSoup(response)
 14 links=re.findall(r'<a.*class="btn".*</a>',html)
 15 #print soup
 16 fin=re.findall(r'http:.*.mp3',links[0])
 17 pr=fin[0].split("'")
 18 print pr[0]
 19 filelink=urllib2.urlopen(pr[0])
 20 name=name + ".mp3"
 21 output=open(name,'wb')
 22 output.write(filelink.read())
 23 output.close()
 24 print 'Cheers !!! Download complete :)'
