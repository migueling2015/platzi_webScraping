import requests
from bs4 import BeautifulSoup

url='https://www.pagina12.com.ar/'

p12=requests.get(url)

dict_content={}

print('#############################################################################################################')
print('#############################################################################################################')
print(p12.status_code)
print('#############################################################################################################')
print('#############################################################################################################')
# print(p12.text)
print('#############################################################################################################')
print('#############################################################################################################')
# print(p12.headers)
print('#############################################################################################################')
print('#############################################################################################################')
# print(p12.request.headers)
print('#############################################################################################################')
print('#############################################################################################################')
# print(p12.cookies)

s = BeautifulSoup(p12.text, 'html.parser')
arreglo=s.find('li',attrs={'class':'sections'}).find_all('li')
array_liks_sections=[]
for i in arreglo:
    linkSection=i.a.get('href')
    array_liks_sections.append(linkSection)
    dict_content[i.a.contents[0]]=[]
    dict_content[i.a.contents[0]].append(linkSection)
    print('{} -- {} \n'.format(i.a.contents[0],linkSection))


def extract_url_article(url_in,use_class):
    p_temp=requests.get(url_in)
    s_temp = BeautifulSoup(p_temp.text, 'html.parser')
    array_container=s_temp.find_all('div',attrs={'class':use_class})
    array_container_resulting=[i.find('h2').find('a').get('href') for i in array_container]
    print(array_container_resulting)

for section in dict_content:
    print('\n{}'.format(dict_content[section][0]))
    extract_url_article(dict_content[section][0],'featured-article__container')
    extract_url_article(dict_content[section][0],'article-box__container')