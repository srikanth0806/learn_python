fp = open("append.py", "r")
text = fp.read()
fp.close()
y = compile(text, "append.py", "exec")
exec(y)