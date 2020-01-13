# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:23:55 2020

@author: PRATMS
"""

import openpyxl


def writeToTxtFileFunction(slno, movieName, movieYear):
    print("write ti txt file function for"+str(slno))
    f = open("top100MovieByIMDb.txt", "a")
    f.write(str(slno) + '\t' + str(movieName) + '\t' + movieYear + '\n')
    f.close()


if __name__ == '__main__':
    print("unexpected calling")
