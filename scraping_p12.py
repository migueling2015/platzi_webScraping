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

    return dict_content

    # print(p12.status_code)
    # print(p12.text)
    # print(p12.headers)
    # print(p12.request.headers)
    # print(p12.cookies)




    # def extract_url_article(url_in,use_class):
    #     p_temp=requests.get(url_in)
    #     s_temp = BeautifulSoup(p_temp.text, 'html.parser')
    #     array_container=s_temp.find_all('div',attrs={'class':use_class})
    #     array_container_resulting=[i.find('h2').find('a').get('href') for i in array_container]
    #     print(array_container_resulting)

    # for section in dict_content:
    #     print('\n{}'.format(section))
    #     print('{}'.format(dict_content[section][0]))
    #     extract_url_article(dict_content[section][0],'featured-article__container')
    #     extract_url_article(dict_content[section][0],'article-box__container')