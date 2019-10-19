import requests
from googlesearch import search 
import bs4
import newspaper as ns 
import re
import tldextract as tld


#example
#                                source_url      source_url_processed                                                URL   fact           bias
#              http://www.villagevoice.com/          villagevoice.com   http://mediabiasfactcheck.com/the-village-voice/   HIGH           left

data = pd.read_csv('data/corpus.csv')

dl=data.values.tolist()


def formatData(dataFrame):
    dl=dataFrame.values.tolist()
    for count in range(dl.len())
        dl[count][4]=mapBias(dl[count][4])
    return dl

def mapBias(bias):
    if(bias=="extreme-right" or bias=="right" or bias =="right-center"):
        return "right"
    elif(bias=="left-center" or bias=="left" or bias=="extreme-left"):
        return "left"
    else:
        return "center"
    


def matchUrl(url,data):
    """
    DESC: given a URL this returns the URLs bias, or
    """
    for row in data: 
        if(url in row[1])
            return row[4] 



def extractDomain(domain):
    """
    returns a domain given a URL
    """
    extracted=tld.extract(domain)
    return extracted.domain


URL="https://www.newyorker.com/news/dispatch/why-lebanons-people-are-turning-on-their-politicians"


article = ns.Article(URL)



html=requests.get(URL).content

soupedFile=bs4.BeautifulSoup(html,features="html.parser")


URL.split("/")


def getRepresentation(url):
    html=requests.get(URL).content
    soupedFile=bs4.BeautifulSoup(html,features="html.parser")
    return soupedFile.title


print(soupedFile.title)
# to search 
query = "youtube"
  

for j in search(query,num=100, stop=100, pause=0): 
    print(j)