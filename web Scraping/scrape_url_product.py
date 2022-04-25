import requests
from bs4 import BeautifulSoup


def scrape_url_prod(url):
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
    #print(html_soup)
    
    with open(r"D:\INPT2\Data mining\DataMining-Project\web Scraping\urls_prod.txt", "a") as urls_prod:
        for i in html_soup.find_all("a",class_="a-link-normal s-no-outline", href=True):
            url_prod="\n"+"https://www.amazon.com"+i["href"]
            #print(url_prod)
            urls_prod.write(url_prod)




#with open(r"D:\INPT2\Data mining\DataMining-Project\web Scraping\url_pages.txt", "r") as url_pages:
#   for url in url_pages:
#        scrape_url_prod(url)


for i in range(2,400):
    url="https://www.amazon.com/s?i=appliances&page={}".format(i)
    scrape_url_prod(url)

print("L'operation successfuly excuted !")
