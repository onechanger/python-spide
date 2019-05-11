from websocket import create_connection
import xlwt
import json 


def ws_send(websocket, message):
	websocket.send(json.dumps(message))
	return websocket.recv()

def json_handle(jsonstr, key= False):
	return json.loads(jsonstr)[key]

def fetch(websocket, message, key):
	return json_handle(ws_send(websocket,message),key)

def write_txt(content_list, text_name):#content_list format [stritem,...]
	temp = open(text_name + '.txt','wb')
	temp.write('\n'.join(content_list).encode('utf-8'))
	temp.close()

def write_excel(content_list, excel_name):#content_list format [[stritem,...],...]
	file = xlwt.Workbook(encoding = 'utf-8')
	table = file.add_sheet(excel_name)
	for i,p in enumerate(content_list):
	    for j,q in enumerate(p):
	        table.write(i,j,q)
	file.save(excel_name + '.xls')

def add_txt(content_list, text_name):
	temp = open(text_name + '.txt','ab')
	temp.write('\n'.encode('utf-8')+'\n'.join(content_list).encode('utf-8'))
	temp.close()

def read_txt(text_name):
	temp = open(text_name + '.txt','r')
	templist = temp.readlines()
	temp.close()
	templast = templist.pop()
	result = []
	for i in templist:
		result.append(i[0:-1])
	result.append(templast)
	return result

def init_get_params(choice, str='', num=1000):
	if(choice == 'get_user'): return { "method": "call","params": [ 2, "lookup_accounts",[str, num] ],"id": 110}
	if(choice == 'start'):return { 'method': "call", 'params': [1, "database", []], 'id': 2 }
	if(choice == 'get_balances'):return { "method": "call", "params": [2, "get_full_accounts", [[str], True]],"id": 8 }

def result_get_username(resultlist):
	temp = []
	for i in resultlist:
		temp.append(i[0])
	return temp 

def get_list_top(list, key):
	temp = list.copy()
	while True:
		if not temp[-1].startswith(key):
			break
		temp.pop()	
	return temp 		

def init_ws_start():
	ws = create_connection("wss://ifast.one/ws")
	ws_send(ws,init_get_params('start'))
	return ws

def get_one_balances(ws, username):
	result = fetch(ws,init_get_params('get_balances', username),'result')
	return result[0][1]['balances']
 	
def balances_handle(balances):
	result = []
	for i in balances:
	    if i["asset_type"] == "1.3.0":
	        result.append("IFS: {}".format(int(i["balance"]) / 100000))
	    if i["asset_type"] == "1.3.1":
	        result.append("CNB: {}".format(int(i["balance"]) / 10000))
	    if i["asset_type"] == "1.3.2":
	        result.append("PAX: {}".format(int(i["balance"]) / 10000))
	    if i["asset_type"] == "1.3.3":
	        result.append("BTC: {}".format(int(i["balance"]) / 100000000))
	    if i["asset_type"] == "1.3.4":
	        result.append("ETH: {}".format(int(i["balance"]) / 1000000))
	    if i["asset_type"] == "1.3.5":
	        result.append("EOS: {}".format(int(i["balance"]) / 1000000))
	    if i["asset_type"] == "1.3.6":
	        result.append("BTS: {}".format(int(i["balance"]) / 1000000))
	    if i["asset_type"] == "1.3.7":
	        result.append("OMG: {}".format(int(i["balance"]) / 1000000))
	    if i["asset_type"] == "1.3.8":
	        result.append("SNT: {}".format(int(i["balance"]) / 1000000))
	    if i["asset_type"] == "1.3.9":
	        result.append("PAY: {}".format(int(i["balance"]) / 1000000))
	return result

def get_one_result(ws, username):
	result = [username]
	balances = get_one_balances(ws, username)
	result.extend(balances_handle(balances))
	return result

def write_all_user(ws):
	result = fetch(ws,init_get_params('get_user','a',1000),'result')
	user_list = get_list_top(result_get_username(result),'w')
	result = fetch(ws,init_get_params('get_user','w',1000),'result')
	user_list.extend(result_get_username(result))
	write_txt(user_list,'user')
	return user_list

def write_all_balances(ws):
	userlist = read_txt('user')
	result =  [['序号','用户名','资产']]
	for username in userlist:
		print(username,' 已完成')
		result.append(get_one_result(ws,username))
	write_excel(result,'balances')
	return result

def main():
	ws = init_ws_start()
	while True:
		option = input('Please enter the operation you want to enter.\nU : Crawling And Write Uer text \nB : Read Username And Crawling Balances\nQ : Quit\n ')
		if option == "U" or option == "u":
			write_all_user(ws)
			print("文本数据已写入")
		if option == "B" or option == "b":
			write_all_balances(ws)
			print("表格数据已写入")
		if option == "Q" or option == "q":
			print("程序已结束")
			break
	ws.close()

if __name__ == '__main__':
	main()