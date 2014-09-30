#Christopher Reeves Web Scraping Tutorial
#simple web spider that returns array of urls. 
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib
import urlparse

import mechanize
from bs4 import BeautifulSoup as soup







# Set the startingpoint for the spider and initialize 
# the a mechanize browser object
url = "http://catalogue.usc.edu/schools/"


f = open('output.html', 'w')
br = mechanize.Browser()


linkCounter = 0
errorCount = 0


# create lists for the urls in queue and visited urls
urls = [url]
visited = [url]
subsections = []







# Store the page's contents
def writeOutput(response):
    f.write("<section id=\"")
    #f.write(" ".join(response.read().partition("<a href=\"http://catalogue.usc.edu/schools/\">The Schools</a> &raquo;")[2].partition("</p></div><!--/#breadcrumb-->")[0].strip().split()).replace(" ", "-").lower())
    f.write("\">")

    #print response.find(name="div", attrs={'id': 'content-main'})

    pageContents = response.read().partition("<!--/#breadcrumb-->")[2].partition("<div class=\"comments-info\">")[0]

    f.write(pageContents)
    f.write("</section>")







# only executes on first visit (root schools page), inits
#   urls with first seed of urls as a queue. On subsequent
#   runs through we're adding pages like a queue stacked on
#   top of this queue.
try:
    br.open(urls[0])
    urls.pop(0)
    for link in br.links():
        newurl =  urlparse.urljoin(link.base_url,link.url)
        #print newurl
        if newurl not in visited and url in newurl:
            visited.append(newurl)
            urls.append(newurl)
            #print newurl
except:
    print "error"
    errorCount = errorCount + 1
    urls.pop(0)

print len(urls)





# Since the amount of urls in the list is dynamic
#   we just let the spider go until some last url didn't
#   have new ones on the webpage
while len(urls)>0:
    try:
        response = br.open(urls[0])
        urls.pop(0)
        linkCounter = linkCounter + 1
        print str(linkCounter) + ")\t" + urls[0] + "\t\t" + str(errorCount) + " errors"
        writeOutput(response)
        
        for link in br.links():
            newurl =  urlparse.urljoin(link.base_url,link.url).partition("#")[0]
            # print newurl
            if newurl not in visited and url in newurl:
                print "New URL: " + newurl
        #         visited.append(newurl)
        #         subsections.append(newurl)
        #         #print newurl
        # urls.insert(0, subsections)
    except:
        #print "error: " + urls[0] 
        errorCount = errorCount + 1
        if len(urls)>0:
            urls.pop(0)







print "done" #visited
