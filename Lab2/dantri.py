from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
#1. Download webpage
url = 'http://dantri.com.vn'
#1.1 Create a connection
conn = urlopen(url)
# #1.2 Read
# data = conn.read()
# #1.3 Decode
html_content = urlopen(url).read().decode('utf-8')
#save html to file
# f = open ('dantri.html', 'wb')
# f.write(html_content)
# f.close()

# # #html_content
# # print(html_content)
# # save html to file
# file= open("dantri.html", "wb")
# # write, binary
# file.writelines(conn)
# file.close()

#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content, 'html.parser')
# find by class
ul = soup.find("ul", 'ul1 ulnew')
# print (ul.prettify())

#3. Extract data
li_list = ul.find_all('li')
file_excel = []
for li in li_list:


    file_excel.append(
        {
            'title' : (li.h4.a.string),
            'link' : (url+li.h4.a['href'])
        }
    )
pyexcel.save_as(records=file_excel, dest_file_name="dantri.xlsx")