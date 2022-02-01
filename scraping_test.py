from bs4 import BeautifulSoup
import requests
  
sample_website='https://stackoverflow.com/questions/780819/how-can-i-unit-test-arduino-code'

page=requests.get(sample_website)

soup = BeautifulSoup(page.content, 'html.parser')

while(True):
    data = soup.findAll('div',attrs={'class':'related js-gps-related-questions'})
    for div in data:
        links = div.findAll('a')
        for a in links:
            if("/questions" in a['href']):
                nextpage = requests.get("https://stackoverflow.com" + a['href'])
                soup = BeautifulSoup(nextpage.content, 'html.parser')
                print("next url title : ",soup.find('title').string)