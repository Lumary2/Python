from bs4 import BeautifulSoup
import requests
import csv

source=requests.get('https://lumarycodes.wordpress.com/').text

soup=BeautifulSoup(source,'lxml')

csv_file=open('articlesBlog.csv','w')
writer=csv.writer(csv_file)
writer.writerow(['headline','content'])
#print(soup)

article=soup.find('article')

headline=article.h1.a.text
#print(headline)

firstParagraph=article.find('div',class_='entry-content').p.text

#print(firstParagraph)

for article in soup.find_all('article'):
    print(article.prettify())
    headline = article.h1.a.text
    print(headline)

    try:
        firstParagraph = article.find('div', class_='entry-content').p.text
    except Exception as e:
        firstParagraph= None

    print(firstParagraph)

    print()
    writer.writerow([headline,firstParagraph])

csv_file.close()