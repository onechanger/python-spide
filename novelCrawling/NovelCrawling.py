from urllib import request
from bs4 import BeautifulSoup
import time

#start
url = "http://m.biqupa.com/1_1618/1065708.html"
url_origin = "http://m.biqupa.com"
url_match = "#pb_next"
content_match = "#nr1"
html_ecode = 'gbk'
flag = 0
text_name = 'novel.txt'

novel = open(text_name,'ab')

def PhonofraphCrawling():
	global url,flag
	for i in range(200):
		try:
			response = request.urlopen(url) # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
		except:
			if flag == 3:
				print('该章节无法爬取:'+ url)
				break
			else:
				time.sleep(1)
				flag += 1
				i -= 1
				continue
		page = response.read()
		page = page.decode(html_ecode)
		soup = BeautifulSoup(page,features="html.parser")
		ele_src = soup.select(url_match)
		ele_content = soup.select(content_match)
		try:
			url = url_origin + ele_src[0]['href']
			text = ele_content[0].text
		except:
			print("该章节无法爬取内容或url请检测:",url)
		novel.write(text.encode('utf-8'))
		print("爬取第 {} 个章节,爬取次数 {} 次".format(i + 1,flag + 1))
		flag = 0
while True:
	option = input('Please enter the operation you want to enter.\nC : Crawling \nP : print now url\nQ : Quit\nE : Empty\n ')
	if option == "C" or option == "c":
		PhonofraphCrawling()
	if option == "P" or option == "p":
		print(url)
	if option == "Q" or option == "q":
		novel.close()
		print("程序已结束请把初始url改为:",url)
		break
	if option == "E" or option == "e":
		novel.close()
		novel = open(text_name,'w')
		novel.write('')
		novel.close()
		novel = open(text_name,'ab')
		print("{}文本内容已清空".format(text_name))

