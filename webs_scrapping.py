import requests
from bs4 import BeautifulSoup
import functions_gears as gears
import scraping_p12_gears as p12
import scraping_p12 as scrap
from datetime import datetime



if __name__ == '__main__':

    dic_p12=scrap.scrap_page('https://www.pagina12.com.ar/')
    print(dic_p12)
