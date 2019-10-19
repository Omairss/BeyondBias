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
    """
    DESC: transforms bias from being 7 categories to simply 3
    """
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




def findMatches(matchNumber,urlList,data):
    """
    DESC: matches a specified number of urls from a list to indexed urls 
    """
    if(MatchNuber<1 or urlList.len()<matchNumber):
        print("invalid match number")
        return []


    counter=0
    matches=[]
    for url in urlList: 
        for count in range(data.len()):
            if(extractDomain(data[count][2])==extractDomain(url))
                counter+=1
                matches.append(url)
        if(counter==matchNumber):
            return matches
    return matches
