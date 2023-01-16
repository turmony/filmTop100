import getData
import getPage

url_ = 'https://www.maoyan.com/board/4?timeStamp=1673858062757&channelId=40011&index=2&signKey=3660e5f896d23a4939b25df287f5358f&sVersion=1&webdriver=false&offset=0'

if __name__ == '__main__':
    data_sum = []
    url_lists = getPage.get_page_url(url_)
    for i in url_lists:
        html = getPage.get_page_html(i)
        data_sum.append(getData.get_data(i))
    for i in data_sum:
        print(i)
