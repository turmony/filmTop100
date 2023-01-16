import requests
from flask import session
from lxml import etree


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/109.0.0.0 Safari/537.36'}


def get_page_html(url):
    response = requests.get(url, headers=header)
    response.close()
    response.encoding = 'utf-8'
    return response.text


def get_page_url(url):
    page_url_lists = []
    for i in range(100):
        if i % 10 == 0:
            # print(i)
            new_url = url[:-1] + '%d' % i
            # print(new_url)
            page_url_lists.append(new_url)
    # print(page_url_lists)
    return page_url_lists


# if __name__ == '__main__':
#     print(get_page_url(url_))

# with open('./numberButtons.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
# print(text)
# html = etree.HTML(text)
#
# numberButtons = html.xpath('//*[@id="app"]/div/div/div[2]/ul')
# print(numberButtons[0])
# result = numberButtons[0].xpath('//li')
# k = 0
# for i in result:
#     k=k+1
# print(k)
# print(result)
# print('---------')
