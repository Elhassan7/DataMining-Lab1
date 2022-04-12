from venv import create
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
    url_current=html_soup.find("span",class_="s-pagination-strip").find_all("a",{"href"})
    print(html_soup)
    print(url_current)

url="https://www.amazon.com/s?i=mobile&rh=n%3A2335752011%2Cp_72%3A2491149011&page=12&pd_rd_r=30305d08-93c6-4f70-aca0-5bdcd0619f0a&pd_rd_w=V3rlu&pd_rd_wg=cnq1i&pf_rd_p=f5c158e1-98f7-4998-94b8-d7306c066086&pf_rd_r=Q0RJ0DQSNB5EM8EWZX6G&qid=1649612117&ref=sr_pg_12"
scrape_url_page(url)