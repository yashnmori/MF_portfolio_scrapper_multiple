
# coding: utf-8

#Necessary Libs
import requests
import bs4
import csv
import pandas as pd
import matplotlib.pyplot as plt
from pandas import ExcelWriter





#Portfolio Holdings URL for all 5 MF Portfolio
url_1 = requests.get('https://www.moneycontrol.com/mutual-funds/axis-small-cap-fund-regular-plan/portfolio-holdings/MAA314')
url_2 = requests.get('https://www.moneycontrol.com/mutual-funds/kotak-small-cap-fund-regular-plan/portfolio-holdings/MKM073')
url_3 = requests.get('https://www.moneycontrol.com/mutual-funds/dsp-small-cap-fund-regular-plan/portfolio-holdings/MDS076')
url_4 = requests.get('https://www.moneycontrol.com/mutual-funds/l-t-emerging-businesses-fund-regular-plan/portfolio-holdings/MCC490')
url_5 = requests.get('https://www.moneycontrol.com/mutual-funds/nippon-india-small-cap-fund/portfolio-holdings/MRC587')



#Creating BS$ object using lxml parser
soup_1 = bs4.BeautifulSoup(url_1.text,'lxml')
soup_2 = bs4.BeautifulSoup(url_2.text,'lxml')
soup_3 = bs4.BeautifulSoup(url_3.text,'lxml')
soup_4 = bs4.BeautifulSoup(url_4.text,'lxml')
soup_5 = bs4.BeautifulSoup(url_5.text,'lxml')


#getting titles from all webpages
a = '_'.join(soup_1.find('title').text.split()[:4])
b = '_'.join(soup_2.find('title').text.split()[:4])
c = '_'.join(soup_3.find('title').text.split()[:4])
d = '_'.join(soup_4.find('title').text.split()[:4])
e = '_'.join(soup_5.find('title').text.split()[:4])





#Creating a list of bs4 objects.
soups = [soup_1,soup_2,soup_3,soup_4,soup_5]





#Getting table from all URL with given ID and Storing it into List

test_list=[]
data_content=[]

for x in soups:
    eco_table = x.find('table', id='equityCompleteHoldingTable')
    for table in eco_table.find_all('tbody'):
        rows= table.find_all('tr')
        for row in rows:
            new_table=row.find_all('td')[0].text.strip()
            test_list += [new_table]
            
        data_content.append(test_list)
        test_list=[]
data_content



print(len(data_content))



#Converting List into Dataframe
dataset = pd.DataFrame(data_content)
dataset



#Dataframe Transpose
dt = pd.DataFrame(dataset.T)
#Adding Titles to New Dataframe
dt.columns = [a,b,c,d,e]
dt


#Saving Dataframe to Excel.
writer = ExcelWriter('F:/New folder/PythonExport.xlsx')
dt.to_excel(writer,index = False, header=True)
writer.save()

