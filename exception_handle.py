
fp = open("test.txt", "w")
fp.write("Hello")
fp.read()


print(fp.closed)
fp.close()

print(fp.closed)

print("good mornign")