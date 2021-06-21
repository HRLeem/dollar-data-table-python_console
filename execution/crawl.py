from bs4 import BeautifulSoup

from selenium import webdriver
from time import sleep

def main(sw):
    driver = selenium_config()
    url = get_url(sw)
    driver.get(url)
    sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    p_price = soup.select_one('#last_last').text.replace(',','')
    round = soup.select_one('#leftColumn > div.clear.overviewDataTable.overviewDataTableWithTooltip > div:nth-child(6) > span.float_lang_base_2.bold').text
    splited = round.strip().replace(',','').split('-')
    # [ p_price, low, avg, high ]
    return [ float(p_price), float(splited[0]), ( (float(splited[0]) + float(splited[1]))/2 ), float(splited[1])]


def selenium_config():
    driver = webdriver.Chrome('/Users/imharam/hr/codes/for_selenium/chromedriver')
    driver.implicitly_wait(3)
    return driver

def get_url(sw):
    if sw == 'dw':
        return 'https://www.investing.com/currencies/usd-krw'
    elif sw == 'dxy':
        return 'https://kr.investing.com/indices/usdollar'
#
# def main(sw):
#     result_html = get_html(sw)
#     result_list = crawl_it(sw, result_html)
#     return result_list
#
# def get_html(sw):
#     if sw == 'dw':
#         req = requests.get('https://www.investing.com/currencies/usd-krw')
#         html = req.text
#     elif sw == 'dxy':
#         req = requests.get('https://kr.investing.com/indices/usdollar')
#         html = req.text
#     return html
#
# def crawl_it(sw, html):
#     if sw == 'dw':
#         soup = BeautifulSoup(html)
#         print(soup)
#     elif sw == 'dxy':
#         soup = BeautifulSoup(html)
#     p_price = soup.select_one('#last_last')
#     round = soup.select_one('#leftColumn > div.clear.overviewDataTable.overviewDataTableWithTooltip > div:nth-child(6) > span.float_lang_base_2.bold')
#     splited = round.split('-').strip()
#     # [ p_price, low, avg, high ]
#     return [ float(p_price), float(splited[0]), ( (float(splited[0]) + float(splited[1]))/2 ), float(splited[1])]