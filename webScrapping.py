# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:44:53 2020

@author: PRATMS
"""

import bs4, requests
import lxml
import listToNestedDict


extractedValueDict = []


def scrapingFunction(url, tagName, className):
    print("scraping web for 100 movies by IMDB start")
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # url = "https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
    res = requests.get(url, verify=False)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # slno=soup.find_all("a",attrs={"class":"fi cn hx hy hz ia"})
    # bookAndAuthors = soup.find_all("strong", attrs={"class": "id ke"})
    ExtractedHTML = soup.find_all(tagName, attrs={"class": className})
    print(type(ExtractedHTML))
    print("extracting data into dict start")

    for i in range(0, len(ExtractedHTML) - 4):
        if len(ExtractedHTML[i].getText()) > 2:
            extractedValueDict.append(ExtractedHTML[i].getText())
            print(ExtractedHTML[i].getText())
            print(type(extractedValueDict))
    #HtmlToDict.HtmlToDictFunction(ExtractedHTML)
    return extractedValueDict



if __name__ == '__main__':
    print("unexpected calling")
