import getPage
from lxml import etree




def get_data(url):
    global film_name, film_data, film_time
    response = getPage.get_page_html(url)
    print(response)
    html = etree.HTML(response)
    dd_lists = html.xpath('//*[@id="app"]/div/div/div[1]/dl//dd')
    print(dd_lists)
    # print(dd_lists[0].xpath('./i/text()')[0])
    film_sum = []
    for i in dd_lists:
        rank = i.xpath('./i/text()')[0]
        print(rank)
        p_lists = i.xpath('./div/div/div[1]//p')
        print(p_lists)

        film_name = p_lists[0].xpath('./a/text()')[0]
        print(film_name)
        film_data = p_lists[1].xpath('./text()')[0]
        film_data = str.strip(film_data)
        print(film_data)
        film_time = p_lists[2].xpath('./text()')[0]
        print(film_time)
        temp = '排名:' + rank + '  ' + film_name + '  ' + film_data + '  ' + film_time
        print(temp)
        film_sum.append(temp)
    print(film_sum)
    return film_sum


if __name__ == '__main__':
    get_data(url_)
