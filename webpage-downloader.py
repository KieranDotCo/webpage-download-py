import urllib2
import sys

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
f = open("test.txt","a") 
website = '<WEBSITE NAME HERE>'

i = 0
while (i < 3000):
   print 'Downloading ' + website + str(i)
   try:
       req = urllib2.Request(website+ str(i), None, headers)
       response = urllib2.urlopen(req)
   except urllib2.HTTPError:
       print 'Could not download page'
   else:
       page = response.read()
       response.close() 
       f.write(page)
   i = i + 1

f.close()
