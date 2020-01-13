# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:03:18 2020

@author: PRATMS
"""
import bs4, requests
import lxml

'''
extractedValueDict = []
urlIMDB={"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt"}

for url in urlIMDB:
    print(url)

url="https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc"   
print("scraping web for 100 movies by IMDB start")
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # url = "https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
res = requests.get(url, verify=False)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
    # slno=soup.find_all("a",attrs={"class":"fi cn hx hy hz ia"})
    # bookAndAuthors = soup.find_all("strong", attrs={"class": "id ke"})
ExtractedHTML = soup.find_all(h3, attrs={"class": "lister-item-header"})
print(type(ExtractedHTML))
print("extracting data into dict start")

for i in range(0, len(ExtractedHTML)):
    if len(ExtractedHTML[i].getText()) > 2:
        extractedValueDict.append(ExtractedHTML[i].getText())
    print("text-->"+str(ExtractedHTML[i].getText()))
            
    
for i in extractedValueDict:
    i="%r"%i

    bookNestedDict.update({i.split('\n')[0]: {'name': i.split('\n')[1], 'year': i.split('\n')[2]}})
    
    print("extracted value count" + str(bookNestedDict))
'''    
bookNestedDict={}
jj='\n50.\nOnce Upon a Time in the West\n(1968)\n'
i="%r"%jj
#jj='asf by hjk'
ff=jj.split('\\n')
bookNestedDict.update({str(i.split('\\n')[1].replace('.', '')): {'movie': i.split('\\n')[2], 'year': i.split('\\n')[3]}})
print(str(bookNestedDict))