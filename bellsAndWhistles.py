from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from newspaper import Article
import requests
from bs4 import BeautifulSoup
def getReadTime(body):
    wc = len(body.split())
    return wc/100
def getToneScore(body):
    opinion = TextBlob(body)
    sentiment = opinion.sentiment.polarity
    return sentiment*100
def getAuthorScore():
    return 85.3
#def getSourceScore()
if __name__ == '__main__':
    url = 'https://www.newyorker.com/news/dispatch/why-lebanons-people-are-turning-on-their-politicians'
    article = Article(url)
    article.download()
    article.parse()
    print(article.authors)
    article.nlp()
    print(article.keywords)
    authors=""
    print(getToneScore(article.text))
    print(str(getReadTime(article.text))+" minutes")
