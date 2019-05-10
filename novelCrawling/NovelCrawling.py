from urllib import request
from bs4 import BeautifulSoup
import random 
import time
from lxml import etree

#start setting
url = "https://m.biqige.com/7_7478/3283740.html"
url_origin = "http://m.biqige.com"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
# url ="https://www.bxwx.la/b/7/7139/3707378.html"
# url_origin = "https://www.bxwx.la/b/7/7139"
# url_match = '//div[@class="bottem1"]/a[4]/@href'
url_match = '//a[@id="pb_next"]/@href'
content_match = "#nr1"
html_ecode = 'gbk'
flag = 1
text_name = 'jueshishenhuang.txt'
novel = open(text_name,'ab')
temp_url = ''
def NovelCrawling():
	global url,flag,temp_url
	i = 1
	while i < 201:
		time.sleep(1)
		try:
			header = {'User-Agent': random.choice(ua_list)}
			request_ = request.Request(url,headers=header)
			response = request.urlopen(request_,timeout=5) 
			page = response.read()
		except:
			if flag == 4:
				print('该章节无法爬取: '+ url,"上一个章节: "+ previous_url,"上上个章节: " + temp_url)
				flag = 1
				break
			else:
				time.sleep(3)
				flag += 1
				continue
		page = page.decode(html_ecode)

		html = etree.HTML(page,etree.HTMLParser())
		ele_src = html.xpath(url_match)

		soup = BeautifulSoup(page,features="html.parser")
		# ele_src = soup.select(url_match)
		ele_content = soup.select(content_match)
		if i > 1:
			temp_url = previous_url
		previous_url = url
		try:
			# url = url_origin + ele_src[0]['href']
			url = url_origin + ele_src[0]
			text = ele_content[0].text
			# print(text)
		except:
			print("该章节无法爬取内容或url请检测: ",url,"上一个章节: " + previous_url,"上上个章节: " + temp_url)
			break
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