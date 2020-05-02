from bs4 import BeautifulSoup
import functions_gears as gears
from datetime import datetime


def obtain_sections(s):
    arreglo=s.find('li',attrs={'class':'sections'}).find_all('li')
    array_liks_sections=[]
    dic_temp={}
    for i in arreglo:
        linkSection=i.a.get('href')
        array_liks_sections.append(linkSection)
        dic_temp[i.a.contents[0]]=[]
        dic_temp[i.a.contents[0]].append(linkSection)
        print('{} -- {} \n'.format(i.a.contents[0],linkSection))
        
    return dic_temp

def extract_url_article(url_in,use_class):
    p_temp=gears.stablish_connection(url_in)
    try:
        len(page_scraping)
        gears.connection_record('errors_log.log',page_scraping[0],'noConnection --{}'.format(datetime.timestamp(datetime.now())))
    except:
        gears.connection_record('conneceteds_log.log',url_in,'Connected --{}'.format(datetime.timestamp(datetime.now())))
        s_temp = BeautifulSoup(p_temp.text, 'html.parser')
        array_container=s_temp.find_all('div',attrs={'class':use_class})
        array_container_resulting=[i.find('h2').find('a').get('href') for i in array_container]
    return array_container_resulting

def obtain_info(s):
    arreglo=[]
    try:
        info=s.find('div',attrs={'class':'time'}).span.get('datetime')
        arreglo.append(info)
    except:
        pass

    try:
        info=s.find('div',attrs={'class':'article-titles'}).h2.contents
        arreglo.append(info)
    except:
        pass

    try:
        info=s.find('div',attrs={'class':'article-text'}).find_all('p')
        for paragraph_text in info:
            arreglo.append(paragraph_text.contents)
    except:
        pass
    
        
    return arreglo