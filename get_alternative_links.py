import pandas as pd
import newspaper
from googlesearch import search
import pdb
import argparse
import tldextract
from datetime import timedelta




def get_url_bias(url, corpus):
    
    try:
        return corpus.loc[corpus['source_url_processed'].str.contains(tldextract.extract(url).domain)]['bias'].values[0]
    except IndexError:
        return 'center'
    
def get_url_fact(url, corpus):
    try:
        return corpus.loc[corpus['source_url_processed'].str.contains(tldextract.extract(url).domain)]['fact'].values[0]
    except IndexError:
        return 'MIXED'
    
def get_search_query(url):

    article = newspaper.Article(url)

    article.download()
    article.parse()
    article.nlp()

    query             = article.title
    date_before       = article.publish_date + timedelta(days=2)
    date_after        = article.publish_date - timedelta(days=2)

    query_time_before = str(date_before.year) +\
                        '-' + str(date_before.month) +\
                        '-' + str(date_before.day)
            
    query_time_after = str(date_after.year) +\
                        '-' + str(date_after.month) +\
                        '-' + str(date_after.day)
            
            
    query = query + ' before:' + query_time_before + ' after:' + query_time_after
        
    return query
    

    
def get_query_results(search_query):
    
    alt_article_lists = [i for i in search(search_query, num = 10)]
    search_results_df = pd.DataFrame(columns = ['link', 'domain', 'title', 'content'])

    search_results_df['link'] = alt_article_lists
    search_results_df['domain'] = search_results_df['link'].apply(lambda x: tldextract.extract(x).domain\
                                                                             + '.' + tldextract.extract(x).suffix)
    
    return search_results_df


def parse_params():

    parser = argparse.ArgumentParser(description='Source Reliability')
    parser.add_argument('--url',             type=str, default='')
    params = parser.parse_args()
    return params




def main():

    url           = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    
    user_params = parse_params()
    url         = user_params.url
    corpus      = pd.read_csv('data/corpus.csv')

    url_bias      = get_url_bias(url, corpus)
    url_fact      = get_url_fact(url, corpus)
    
    query         = get_search_query(url)
    query_results_df = get_query_results(query)
    query_results_df = query_results_df.fillna('')


    search_results_df = pd.merge(corpus, query_results_df, left_on = 'source_url_processed', right_on = 'domain')
    search_results_df = search_results_df[~search_results_df['bias'].str.replace('-', ' ').str.contains('right')]
    
    search_results_df.to_csv('results/search_results.csv')

    return search_results_df
    #return search_results_df[~search_results_df['bias'].str.replace('-', ' ').str.contains(url_bias)]



if __name__ == '__main__':

    main()

