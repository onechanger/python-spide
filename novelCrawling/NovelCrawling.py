from urllib import request
from bs4 import BeautifulSoup
import time

#start setting
url = "http://m.biqupa.com/1_1618/4020575.html"
url_origin = "http://m.biqupa.com"
url_match = "#pb_next"
content_match = "#nr1"
html_ecode = 'gbk'
flag = 1
text_name = 'novel.txt'
novel = open(text_name,'ab')

def NovelCrawling():
	global url,flag
	i = 1
	while i < 201:
		try:
			response = request.urlopen(url,timeout=5) 
			page = response.read()
		except:
			if flag == 4:
				print('该章节无法爬取:'+ url,"上一个url:"+ previous_url)
				flag = 1
				break
			else:
				time.sleep(1)
				flag += 1
				continue
		page = page.decode(html_ecode)
		soup = BeautifulSoup(page,features="html.parser")
		ele_src = soup.select(url_match)
		ele_content = soup.select(content_match)
		previous_url = url
		try:
			url = url_origin + ele_src[0]['href']
			text = ele_content[0].text
		except:
			print("该章节无法爬取内容或url请检测:",url)
		novel.write(text.encode('utf-8'))
		print("爬取第 {} 个章节,爬取次数 {} 次".format(i,flag))
		i += 1
		flag = 1

while True:
	option = input('Please enter the operation you want to enter.\nC : Crawling \nP : Print now url\nE : Empty the text\nQ : Quit\n ')
	if option == "C" or option == "c":
		NovelCrawling()
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