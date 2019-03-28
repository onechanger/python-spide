# solove NO.1

test_str = "['eərɪə]".encode('utf-8')
print(test_str)#b"['e\xc9\x99r\xc9\xaa\xc9\x99]"
print(type(test_str))#<class 'bytes'>
# test = open("test.txt",'ab')
# test.write(test_str)
# test.close()


test_str = test_str.decode('utf-8')
print(test_str)#['eərɪə]
print(type(test_str))#<class 'bytes'>
# test = open("test.txt",'a+')
# test.write(test_str)
# test.close()
# error

test_str = u"['eərɪə]"#equerl to first /*charset = utf-8
print(test_str)#['eərɪə]
print(type(test_str))#<class 'str'>
# test = open("test.txt",'a+')
# test.write(test_str)
# test.close()
#error

test_str = r"['eərɪə]"#\ not effect
print(test_str)#['eərɪə]
print(type(test_str))#<class 'str'>
# test = open("test.txt",'a+')
# test.write(test_str)
# test.close()
#error


'only first can be write'
# test_str = test_str.undecode('utf-8')
# test = open("test.txt",'ab')
# test.write(test_str)
# test.close()

# test = open("test.txt",'a+')
# test_str = u"['eərɪə]"
# test.write(test_str)
# test.close()

test_str = "first\tend\n"
test = open("test.txt",'a+')
test.write(test_str)
test.close()
test_str = "first12345678end\n"
test = open("test.txt",'a+')
test.write(test_str)
test.close()
test = open("test.txt",'r')
teststr = test.readlines()
test.close()
for i in teststr:
	print(i)