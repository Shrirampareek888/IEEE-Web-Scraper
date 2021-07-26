
import urllib
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import os
a = 7546500
url = 'https://ieeexplore.ieee.org/document/'
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
print('Welcome To IEEE Scraper!')
print('Enter the starting Document ID (choose -1 for default id): ')
id = int(input())
if id!=-1:
    a=id;
print("Enter The Quantity of Papers to Scrape :")
rng = int(input())
for b in tqdm(range(0,rng)):
    file = open('file.txt','w')
    c = url + str(a)
    page = urllib.request.urlopen(c)
    soup = BeautifulSoup(page, features='html.parser')
    P = soup.title.string
    
    urllib.request.urlretrieve(c,'file.txt')
    file.close()
    searchfile = open('file.txt', 'r')
    for line in searchfile:
        if "chronOrPublicationDate" in line:
            x=line
            #print(x)
    o=x.rfind("publicationDate")
    i=[]
    j=[]
    z=0
    t=0
    y=0
    q = x.count('"firstName":')
    if(q==0):
        H.append(P)
        A.append(b)
        B.append('-')
        G.append(x[o+18:o+27])
    else:        
        while( t<1):
            z=x.index('"firstName":',z+1)
            y=x.index('"lastName":',y+1)
            i.append(z)
            j.append(y)
            t=t+1
        #print(x[o+18:o+27])
        #print(x[i[0]+13:j[0]-2])
    
        searchfile.close()
        H.append(P)
        A.append(b)
        B.append(x[i[0]+13:j[0]-2])
        G.append(x[o+18:o+27])
    a=a+1
    df=pd.DataFrame(A,columns=['Srno'])
    df['Title'] = H
    df['Lead Author']=B
    df['Date of Publication']=G
    df.style.set_properties(**{'text-align': 'center'})
    export_csv = df.to_csv (r'ScrapedData-'+timestr+'.csv', index = False, header=True)
file.close()
os.remove('file.txt')
print('\nScraping Completed!')
print('Scraped Data is present in ScrapedData-'+timestr+'.csv')
print('Happy Scraping!')
