# Python_Page_Spider_Web_Crawler_Tutorial
# from https://www.youtube.com/watch?v=SFas42HBtMg&list=PLa1r6wjZwq-Bc6FFb9roP7AZgzDzIeI8D&index=3
# Spider algorithm.
# You need to EXECUTE the file in Shell, e.g.  execfile("nytimes/scrape.py")
# First open cmd.  Then cd C:\Users\Joh\Documents\Python Scripts\Web Crawler Projects\nytimes.
# Then enter Python Scrape.py

import urlparse
import urllib
#import urllib.request for Python3?
from bs4 import BeautifulSoup
import csv
import requests

with open ('data.csv') as f:
        f_csv = csv.reader(f)
        #headers = next(f_csv)

        for headers in f_csv:
                #print headers
                urls = headers
                visited = [urls]

                while len(urls) >0:
                        try:
                                htmltext = urllib.urlopen(urls[0]).read()
                                #r = requests.get(urls[])
                                #urls.pop(0)
                        except:
                                print urls[0]

                        soup = BeautifulSoup(htmltext)

                        urls.pop(0)

##                        print headers
##                        print "STARTS HERE:   \n"
##                        print "\n" + "\n"
##                        print soup.findAll('a', href=True)
##
##                        print "\n\n\n"

                        items = soup.findAll('a', href=True)
                        
                        print headers
                        
                        
                        items2 = "STARTS HERE:\n\n" + str(items)
                        saveFile = open ('crawl_findall.txt','w')
                        saveFile.write(items2)
                        saveFile.close()
                        print items2

'''
        for tag in soup.findAll('a', href=True):
		# print tag
		# print tag['href'] # is you just want to print href
		tag['href'] = urlparse.urljoin(url,tag['href'])
		#print tag['href']
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href']) # historical record, whereas above line is temporary stack or queue.
		print visited	
'''
