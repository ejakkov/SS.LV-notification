import requests
from bs4 import BeautifulSoup
import sys
import subprocess

def request():
    URL = "https://www.ss.com/lv/transport/cars/chrysler/voyager/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    div_element = soup.find('div', attrs={'class': 'my-class', 'id': 'my-id'})
    table = soup.find('table', attrs = {'cellpadding':'2', 'border':'0', 'cellspacing':'0', 'border': '0', 'align': 'center'}) # atrodam nepieciešamo tabulu, izmantojot atribūtus
    return table

def manipulateData():
    table = request()
    rows = table.find_all('tr')
    rows = rows[1:-1]
    
    infoList = []
    for row in rows:
        mainInfo = row.find_all('td', class_='msga2-o pp6')
        # sales ad contains 3 'td' with the relevant class, purchase ad - 4 (we are not interested in those) 
        year=volume=price=mileage='-1' 
        if len(mainInfo)==3:
            year, volume, price = [str(a.get_text()) for a in row.find_all('td', class_='msga2-o pp6')]
            price = price.replace(',', '.') # for csv formatting
        link = 'https://www.ss.com' + str(row.find("a",{"class":"am"}).get("href"))
        mileage = row.find('td', class_='msga2-r pp6')
        if mileage is True:
            mileage = str(mileage.get_text())
        else:
            mileage = '-1'
        stringToAppend = year + ',' + volume + ',' + mileage + ',' + price.split(' ')[0] + ',' + link + '\n'
        infoList.append(stringToAppend)
    return infoList


def sortList(scrapedInformation):
    listToWrite =[]
    for line in scrapedInformation:
        line = line.split(",")
        if line[0]!= '-1' and int(line[0])<2000 :
            listToWrite.append(', '.join(line))
    return listToWrite

def writeList(listToWrite):
    with open('table.txt', 'w', encoding='utf8') as f:
        for line in listToWrite:
            f.write(line)

def readText():
    listToReturn = []
    with open('table.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            listToReturn.append(line)
    return listToReturn

def checkMatches(newInfo, oldInfo):
    if(newInfo != oldInfo):
        writeList(newInfo)
        subprocess.run(['python', 'mail_sender.py'])


checkMatches(sortList(manipulateData()), readText())