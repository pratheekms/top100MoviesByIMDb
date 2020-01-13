# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:08:49 2020

@author: PRATMS
"""

#extractedValueDict = []

bookNestedDict = {}
import time


def listToDictFunction(extractedValueDict, extractedValueCount=1):
    # extractedValueCount = 1
    print("extracting data into booknesteddict")
    '''
    for i in range(0, len(ExtractedHTML) - 4):
        if len(ExtractedHTML[i].getText()) > 2:
            extractedValueDict.append(ExtractedHTML[i].getText())
            print(ExtractedHTML[i].getText())
'''
    for i in extractedValueDict:
        i="%r"%i
        print("i as raw text "+i)
        time.sleep(2)
        bookNestedDict.update({str(i.split('\\n')[1].replace('.', '')): {'movie': i.split('\\n')[2], 'year': i.split('\\n')[3]}})
        
        print("extracted value count " + str(extractedValueCount))
        extractedValueCount+=1
    return bookNestedDict

if __name__ == '__main__':
    print("unexpected calling")
