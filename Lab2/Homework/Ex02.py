from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
html_content = urlopen(url).read().decode('UTF-8')

soup = BeautifulSoup(html_content, 'html.parser')

title = soup.find('div', {'id' : "divTableHeader"})
table = soup.find('table', {'id': "tableContent"})
tr_list = table.find_all('tr', 'r_item ') + table.find_all("tr", 'r_item_a')
td_title_list = title.find_all('td')
statistics = []
for tr in tr_list:
    item = {}
    td_list = tr.find_all('td')
    for i in range (5):
        if i == 0:
            chuoi = td_list[i].string.replace("\r","").replace("\n","").replace('\xa0',"")
            td_title_list[i].string = "None"
            item[td_title_list[i].string] = chuoi
        else:
            item[td_title_list[i].string.replace("\r","").replace("\n","").replace('\xa0',"")] = td_list[i].string
    statistics.append(item)
print (statistics)
pyexcel.save_as(records = statistics, dest_file_name = 'table.xlsx')