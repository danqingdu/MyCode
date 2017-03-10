1. 每次处理一个字符
# 调用内建的list，用字符串作为参数
thelist = list(thestring)

#也可以不创建一个列表，直接用for
for c in thestring:
	do_something_with(c)

#或者用列表推导中的for
result = [do_something_with(c) for c in thestring]

#再或者，可以用内建的map函数，每取得一个字符就调一次处理函数
result = map(do_something, thestring)
