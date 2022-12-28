# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 02:49:26 2022

@author: Lenovo
"""

from bs4 import BeautifulSoup
import requests
import re
import csv

# liste=[["http://www.rochade-goettingen.de/index.html","index-alt.txt"],
#        ["http://www.rochade-goettingen.de/aktuelles-2.html","aktuelles-alt.txt"],
#        ["http://www.rochade-goettingen.de/naechste-termine-2.html]","naechste-termine-alt.txt"],
#        ["http://www.rochade-goettingen.de/mitglieder-2.html]","mitglieder-alt.txt"],
#        ["http://www.rochade-goettingen.de/unsere-mannschaften-2.html","unsere-mannschaften-alt.txt"],
#        ["http://www.rochade-goettingen.de/vereinsmeisterschaft-2.html","vereinsmeisterschaft-alt.txt"],
#        ["http://www.rochade-goettingen.de/schnell-blitz-vm.html","schnell-blitz-vm-alt.txt"],
#        ["http://www.rochade-goettingen.de/turniere-ausserhalb-2.html","turniere-außerhalb-alt.txt"],
#        ["http://www.rochade-goettingen.de/schulschach-2.html","schulschach-alt.txt"],
#        ["http://www.rochade-goettingen.de/dwz-liste.html","dwz-liste.txt"],
#        ["http://www.rochade-goettingen.de/rekorde-und-freunde-1.html","rekorde-und-freunde-alt.txt"],
#        ["http://www.rochade-goettingen.de/lustiges-2.html","lustiges-alt.txt"],
#        ["http://www.rochade-goettingen.de/verschiedenes-1.html","verschiedenes-alt.txt"],
#        ["http://www.rochade-goettingen.de/vorstaende-news-links.html","vorstaende-news-links-alt.txt"],
#        ["http://www.rochade-goettingen.de/statut.html","statut-alt.txt"],
#        ["http://www.rochade-goettingen.de/chroniken-2015-2021.html","chroniken-2015-2021.txt"],
#        ["http://www.rochade-goettingen.de/chroniken-2008-2014.html","chroniken-2008-2014.txt"],
#        ["http://www.rochade-goettingen.de/fruehere-beitraege.html","fruehere-beitraege-alt.txt"],
#        ["http://www.rochade-goettingen.de/datenschutzerklaerung.html","datenschutzerklaerung-alt.txt"],
#        ]

liste=[["http://www.rochade-goettingen.de/turniere-ausserhalb-2.html","turniere-außerhalb-alt.txt"],
       ["http://www.rochade-goettingen.de/fruehere-beitraege.html","fruehere-beitraege-alt.txt"],
       ["http://www.rochade-goettingen.de/naechste-termine-2.html","naechste-termine-alt.txt"],
       ]

for element in liste:
    
    x=element[0]
    print(x)
    print(element[1])
    URL=x
    website = requests.get(URL)
    results = BeautifulSoup(website.content, 'html.parser')
    text = str(results)
    try:    
        with open (element[1],"a") as file:
            file.write(text)
    except:
        pass            
    
