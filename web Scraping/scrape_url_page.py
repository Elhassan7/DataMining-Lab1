from venv import create
from click import open_file
import requests
from bs4 import BeautifulSoup


def scrape_url_page(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    pg=requests.get(url, headers=headers)

    html_soup=BeautifulSoup(pg.text,'html.parser')
    with open(r"D:\INPT2\Data mining\DataMining-Project\web Scraping\url_pages.txt", "a") as url_pages:
        for i in html_soup.find("span",class_="s-pagination-strip").find_all("a",href=True):
            url_pag="\n"+"https://www.amazon.com"+i["href"]
            if not in_urls(url):
                url_pages.write(url_pag)
    
    print(len(html_soup))


def in_urls(url):   
    url_pages=open_file(r'D:\INPT2\Data mining\DataMining-Project\web Scraping\url_pages.txt','r') 
    for urls in url_pages:
        urls=urls[:-1]
        if(url == urls ):
            return True
    return False

j=0
for i in range(10):
    url_pages=open_file(r'D:\INPT2\Data mining\DataMining-Project\web Scraping\url_pages.txt','r')
    for url in url_pages:
        #url= url[:-1]
        #print(url)
        scrape_url_page(url)
        j+=1


print("Fin of scraping {} urls of web ages !".format(j))