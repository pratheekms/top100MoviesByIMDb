# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:03:18 2020

@author: PRATMS
"""

urlIMDB={"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt",
	"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt"}

for url in urlIMDB:
    print(url)