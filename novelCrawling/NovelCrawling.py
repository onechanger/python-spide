from urllib import request
from bs4 import BeautifulSoup

# url = r'http://dict.youdao.com/search?q='+ i +'&keyfrom=new-fanyi.smartResult'#r'http://dict.youdao.com/search?q=look&keyfrom=new-fanyi.smartResult'、
novel = open('novel.txt','ab')
#start
url = "http://m.biqupa.com/1_1618/1065474.html"
try:
	for i in range(200):
		response = request.urlopen(url) # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
		page = response.read()
		page = page.decode('gbk')
		soup = BeautifulSoup(page,features="html.parser")
		ele_src = soup.select("#pb_next")
		url = "http://m.biqupa.com" + ele_src[0]['href']
		ele_content = soup.select("#nr1")
		novel.write(ele_content[0].text.encode('utf-8'))
	novel.close()
except:
	print(url)
# url = 

  


