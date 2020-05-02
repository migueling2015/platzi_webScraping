import requests
from bs4 import BeautifulSoup
import functions_gears as gears
import scraping_p12_gears as p12
from datetime import datetime

def scrap_page(url):

    page_scraping=gears.stablish_connection(url)

    try:
        len(page_scraping)
        gears.connection_record('errors_log.log',page_scraping[0],'noConnection --{}'.format(datetime.timestamp(datetime.now())))
    except:
        gears.connection_record('conneceteds_log.log',url,'Connected --{}'.format(datetime.timestamp(datetime.now())))
        s = BeautifulSoup(page_scraping.text, 'html.parser')

        dict_content=p12.obtain_sections(s)
        
        for key in dict_content:
            page_scraping=gears.stablish_connection(dict_content[key][0])
            try:
                len(page_scraping)
                gears.connection_record('errors_log.log',page_scraping[0],'noConnection --{}'.format(datetime.timestamp(datetime.now())))
            except:
                gears.connection_record('conneceteds_log.log',dict_content[key][0],'Connected --{}'.format(datetime.timestamp(datetime.now())))
                s = BeautifulSoup(page_scraping.text, 'html.parser')

            for section in dict_content:
                print('\n{}'.format(section))
                print('{}'.format(dict_content[section][0]))
                dict_content[section].append(p12.extract_url_article(dict_content[section][0],'featured-article__container'))
                dict_content[section].append(p12.extract_url_article(dict_content[section][0],'article-box__container'))

            return dict_content




