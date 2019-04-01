from urllib import request
from bs4 import BeautifulSoup
import time
word_str ='''abort
accept
address
align
animation
application
area
Array
async
asynchronously
attributes
background
base
blockquote
blur
body
bold
Boolean
border
Bottom
button
canvas
case
catch
charset
children
classname
clear
clickable
client
Collapse
color
column
comment
concat
console
container
content
continue
cookie
coordinate
count
cursor
data
Date
Decoration
default
delete
detail
direction
DOCTYPE
download
draggable
drop-down
element
enable
error
event
external
fetch
filter
flex
float
flow
focus
font
footer
form
frame
geolocation
Global
graphics
grow
head
height
hidden
highlight
history
href
hyperlink
icon
image
important
Indent
index
input
instance
invalid
JavaScript
join
JSON
justify
label
language
loop
lowercase
machine
margin
mark
Math
max
measurement
method
multiline
multiple
mute
navigation
null
Number
opacity
Operators
order
Orientation
Origin
outline
overflow
Overrides
padding
parameter
paste
pattern
pause
perspective
placeholder
position
preferences
private
promise
protocol
readonly
RegExp
relative
remove
repeat
Represent
resize
resources
resume
return
sample
sandbox
scope
screen
search
section
Shadow
Shrink
size
sound
source
span
Specifies
src
Statements
step
Storage
String
strong
style
switch
table
tag
target
template
throw
title
Transfer
translate
type
undefined
unload
uppercase
validate
value
variable
versions
Visibility
visible
wait
Website
while
width
wrap
write'''



zh_str = '''中断、中止
 接受
 地址
 排列
 动画
 应用
 区域
 数组
 异步
 异步
 属性
 背景
 基础
 标记长的引用
 使模糊
 身体
 黑体的、更粗的
 布尔型
 边框
 底部
 按钮
 帆布
 例子
 捕捉
 字符集
 孩子
 类名
 清除
 可点击
 委托人
 合并、关闭
 颜色
 行
 评论、意见
 连接
 控制台
 容器
 内容
 继续
 本地存储
 坐标
 记数、数
 光标
 数据
 日期
 装饰、修饰
 系统默认值
 删除
 详述
 方向
 文档类型
 下载
 可拖动的
 下拉列表
 元素
 使能够
 错误
 事件
 外部
 取
 过滤器
 弹性
 浮点
 流动
 焦点
 字体
 页脚
 表单
 框
 地理定位
 全球的
 图形、图表算法
 生长、发育
 头
 高度
 隐藏
 强调
 历史
 连接
 超链接
 图标
 图片
 重要的
 缩进
 指标、指数
 输入
 例子
 无效的
 Script语言
 连接、结合
 json符号对象
 排列整齐
 标签
 语言
 重复
 小写字母
 机器装置
 外边框
 标记
 计算算数
 最大
 测量
 方法
 多线
 倍数
 静音
 导航栏
 空
 数字
 透明值
 操作者
 命令
 方向
 起源
 轮廓
 溢出
 复写，重写
 内边距
 参数
 黏贴
 模式
 暂停
 立体效果
 占位符
 位置
 参数选择
 私有的
 承诺、保证
 草案
 只读的
 正则表达式
 相对定位
 移动
 重复
 构成
 调整大小
 资源
 简历
 返回
 样品
 沙盘
 范围
 屏幕
 搜索
 部分
 阴影
 收缩
 大小
 声音
 来源
 行内元素标签
 指定
 来源
 声明
 步骤
 仓库
 字符串
 强调文本标签
 样式
 分支
 列表
 标签
 目标
 模板
 抛
 标题
 转移
 翻译
 类型
 不明确的
 退出
 大写字母
 生效
 值
 可变的
 版本
 能见度
 可见的
 等待
 网站
 当..时候
 宽度
 包装
 书写'''

#
word_list = word_str.split()
zh_list = zh_str.split()
# print(len(word_list))
# print(len(zh_list))
# for i in zh_list:
#       print(i + word_list[flag])
#       flag += 1
temp = open('tt.txt','wb')
enstr = ''
# for i in word_list:
#       url = r'http://dict.youdao.com/search?q='+ i +'&keyfrom=new-fanyi.smartResult'#r'http://dict.youdao.com/search?q=look&keyfrom=new-fanyi.smartResult'
#       response = request.urlopen(url) # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
#       page = response.read()
#       page = page.decode('utf-8')
#       soup = BeautifulSoup(page)
#       print(flag)
#       # try:
#       ele = soup.select("span .phonetic")


#       if len(ele) > 1 :
#             enstr +=(i + " "+  zh_list[flag] + "  " + "美:"+ele[1].text + '\n'  )
#       elif len(ele) == 1:
#             enstr +=(i + " "+  zh_list[flag] + "  " + "音标:"+ ele[0].text + '\n')
#       else: 
#             enstr +=(i + " "+  zh_list[flag] + "  " + ":查不到音标" + '\n')
#       flag += 1
#       # except:
#       #       print('error:'+ i)

# url_match = "#pb_next"
content_match = "span .phonetic"
html_ecode = 'utf-8'
flag = 1
text_name = 'phonofraph.txt'
novel = open(text_name,'ab')
url =''
def PhonofraphCrawling():
      global flag,url
      i = 0
      times = len(word_list)
      while i < times:
            url = r'http://dict.youdao.com/search?q='+ word_list[i] +'&keyfrom=new-fanyi.smartResult'
            try:
                  response = request.urlopen(url,timeout=5) 
                  page = response.read()
            except:
                  if flag == 4:
                        print('该单词无法爬取:'+ url)
                        flag = 1
                        break
                  else:
                        time.sleep(1)
                        flag += 1
                        continue
            page = page.decode(html_ecode)
            soup = BeautifulSoup(page,features="html.parser")
            # ele_src = soup.select(url_match)
            ele_content = soup.select(content_match)
            if len(ele_content) > 1 :
                  str_temp = (word_list[i] + "  "+  zh_list[i] + "  " + "美: "+ele_content[1].text + '\n' + "\n" )
            elif len(ele_content) == 1:
                  str_temp = (word_list[i] + "  "+  zh_list[i] + "  " + "音标: "+ ele_content[0].text + '\n' + "\n")
            else: 
                  str_temp = (word_list[i] + "  "+  zh_list[i] + "  " + " :查不到音标" + '\n' + "\n")

            novel.write(str_temp.encode('utf-8'))
            print("爬取第 {} 个单词,爬取次数 {} 次".format(i+1,flag))
            i += 1
            flag = 1

while True:
      option = input('Please enter the operation you want to enter.\nC : Crawling \nP : Print now url\nE : Empty the text\nQ : Quit\n ')
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
