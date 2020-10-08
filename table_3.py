from typing import Any
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

 

StartDate = '08/08/2020'
#StartDate = input('Enter Start Date (MM/DD/YYYY):')
print('Start Date", ' +StartDate)

 

EndDate = input ('Enter End Date (MM/DD/YYYY) or Enter for Same Date as StartDate:' )
if EndDate == "":
   EndDate = StartDate
print('End Date", ' +EndDate)

 

url = "https://mcsapps.ciena.com/OCS_RC/ModuleManufacturing/TR4AnAOAllData.asp?AO=20606&FromDate={StartDate}%2012%3A00%20AM&ToDate={EndDate}%2011%3A59%20PM&PartMask=%25&Site=All%20Sites%23%25"
#url = "https://mcs.ciena.com/InetReports/AssemblyHistory/ResultsByAO.asp?SN=NNTMRT112ND8&PN=NTK540BC-820&R=008"
html = urlopen(url)

 

soup = BeautifulSoup(html, 'lxml')

 

print('\n' + soup.title.string +'\n')
print('\n' + soup.td.string +'\n')
#print(soup.find_all ('td') )

 

#soup.find_all('a')

 

print(soup.prettify())  #this prints out all the data in xml format..

 

 


type(soup)
bs4.BeautifulSoup
title = soup.title
print(title)
#text = soup.get_text()
#print(text)
rows = soup.find_all('tr')
#print(rows[7:10])
for row in rows[4:]:
    row_td = row.find_all('td')
    #print(row_td)
    type(row_td)
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    print(cleantext)  #this is for the text as per console
import re
list_rows = []
for row in rows[4:]:
    cells = row.find_all('td')
    str_cells = str(cells[0:12])
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)  #this is for the text as per consolw


type(clean2)
df = pd.DataFrame(list_rows)
df.head(10)
df1 = df[0].str.split(',', expand=True)
df1.head(10)
df1[0] = df1[0].str.strip('[')
df1.head(10)
 

col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels[0:12])
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)
df2 = pd.DataFrame(all_header)
df2.head(10)
df3 = df2[0].str.split(',', expand=True)
df3.head(10)
frames = [df3, df1]
 

df4 = pd.concat(frames)
df4.head(20)
df5 = df4.rename(columns=df4.iloc[0])
df5.head(20)
df6 = df5.drop(df5.index[0])
df6.head(20)
