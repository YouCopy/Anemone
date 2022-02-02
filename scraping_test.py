from bs4 import BeautifulSoup #pip install beautifulsoup4
import requests #pip install requests
  
start = 'https://stackoverflow.com/questions/780819/how-can-i-unit-test-arduino-code' #start page, can be pretty much any question page on stackoverflow

page = requests.get(start) #basically used to "click" on a new webpage

soup = BeautifulSoup(page.content, 'html.parser') #sets bs4 to scrape the website we just "clicked" on

while(True): #should be a way to do this without this while statement, but I haven't looked into it yet
    data = soup.findAll('div',attrs={'class':'related js-gps-related-questions'}) #finds everything listed under this class
    for div in data:
        links = div.findAll('a') #finds every a tag listed in the data variable
        for a in links:
            if("/questions" in a['href']): #the links we're looking for here all have /questions in the url so we check to see if they're present
                nextpage = requests.get("https://stackoverflow.com" + a['href']) #essentially clicks on a new link, at the moment only the last page gets checked for new links
                soup = BeautifulSoup(nextpage.content, 'html.parser')
                print("Next page: ",soup.find('title').string) #prints out the header of the current page

#at the moment, kind of a clusterfuck that really needs to be cleaned up, but it works well enough as a basic proof of concept, does easily get stuck in an infinite loop at the moment
#need to optimize and probably click on every page to get their links ad infinitum, that way if we run into a dead end we can just switch to another branch?
#also at the moment only clicks on links in one specific area of the page, should probably expand it to more sections to get more links
#also also need to find workarounds to stackoverflow limiting the amount of pages that can be clicked before getting timed out