import re

text = """or 	YESREG (from your  mobile number) send it to 9840909000
For Account balance	YESBAL <customer ID> send it to 9840909000
Block credit Card	BLKCC <space><last 4 digit> send it  to 9840909000 
Missed call banking For account balance	Number 09223921111 reg2389"""
# y = re.search("0?\d" , text)
# print(y.group())
# y = re.findall("0?\d" , text)
# print(y)
# y = re.findall("\d" , text)
# print(y)
# y = re.findall("0?\d" , text)
# print(y)
# y = re.findall("0\d" , text)
# print(y)
# y = re.findall("1?\d" , text)
# print(y)
# y = re.findall("\d+" , text)
# print(y)
# y = re.findall("\d*" , text)
# print(y)
# y = re.findall("\d{2 , 5}" , text)
# print(y)
# y = re.findall("\d{, }" , text)
# print(y)
# y = re.findall("\d{10}" , text)
# print(y)
# y = re.findall("\d{2}" , text)
# print(y)
# y = re.findall("\d{30}" , text)
# print(y)
# y = re.findall("\d{1}" , text)
# print(y)
# y = re.findall("[a-z]+" , text)
# print(y)
# y = re.findall("[a-z]*" , text)
# print(y)
# y = re.search("[a-z]+" , text)
# print(y.group())
y = re.search("[a-z]*" , text)
print(y.group())
y = re.findall("[a-z]*" , text)
print(y)

# y = re.search("reg\d{4}$", text)
# print(y.group())
# mail = "hello sir my mail id is nafajsGJH67435429ga@gmail.com. kindly revert to" \
#        "this mmail id"
# y = re.search("[a-z][a-zA-Z0-9.]*@[a-zA-Z0-9]+.com", mail)
# print(y.group())