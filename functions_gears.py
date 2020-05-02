import requests
from bs4 import BeautifulSoup

def error_manager(func):
    def wrapper(*args):
        try:
            val_temmp=func(*args)
        except Exception as e:
            val_temmp=[*args, e]
        return val_temmp
    return wrapper

def connection_record(file_name,url_log,url_mess):
    file_error_log=open(file_name,'a')
    file_error_log.writelines(url_log)
    file_error_log.writelines('\n   {}\n'.format(url_mess))
    file_error_log.close()

@error_manager
def stablish_connection(url):
    return requests.get(url)
