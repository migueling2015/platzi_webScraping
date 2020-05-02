from bs4 import BeautifulSoup

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
