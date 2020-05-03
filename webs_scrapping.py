import requests
from bs4 import BeautifulSoup
import functions_gears as gears
import scraping_p12_gears as p12
import scraping_p12 as scrap
from datetime import datetime
import winsound



if __name__ == '__main__':

    dic_p12=scrap.scrap_page('https://www.pagina12.com.ar/')
    # print(dic_p12)

    array_data=[]

    # for url in dic_p12['El país']:
    #     array_data.append(scrap.extract_from_a_list(url))

    # for url in dic_p12['El país']:
    #     array_data.append(scrap.extract_from_a_list(url))



    array_data.append(scrap.extract_from_a_list(dic_p12['El país'][1]))

    array_data.append(scrap.extract_from_a_list(dic_p12['El país'][2]))

    print(scrap.extract_from_a_list(dic_p12['El país'][2]))


    # print(array_data)
    file_content_reg=open('{}----Content.txt'.format(datetime.timestamp(datetime.now())),'w')
   
        
    file_content_reg.close()

    
    frequency = 5000  # Set Frequency To 2500 Hertz
    duration = 20  # Set Duration To 1000 ms == 1 second
    
    try:
        winsound.Beep(frequency, duration)
        frequency = 2500  # Set Frequency To 2500 Hertz
        winsound.Beep(frequency, duration)
        frequency = 1500  # Set Frequency To 2500 Hertz
        winsound.Beep(frequency, duration)
        frequency = 500  # Set Frequency To 2500 Hertz
        duration = 960
        winsound.Beep(frequency, duration)
    except:
        print('TERMIANDO')
