from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs/'

html_content = urlopen(url).read().decode('UTF-8')

soup = BeautifulSoup(html_content, 'html.parser')

sec = soup.find ('section', 'section chart-grid')
div = sec.find ('div')
ul = div.find ('ul')

li_list = ul.find_all('li')
songlist = []
for li in li_list:
    songlist.append(
        {
            'title' : (li.h3.a.string),
            'artists' : (li.h4.a.string)
    }
    )
pyexcel.save_as(records = songlist, dest_file_name = "Songlist.xlsx")