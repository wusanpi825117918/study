'''
字典中的数据访问
'''
d = {'one': '星期一', 'two': '星期二', 'three': '星期三','haha':'周末'}

print(d['one'])
print(d.get('one'))

# print(d['onee'])
#  下标方式 在访问数据时，如果key不存在，会报错
# get方法方式 访问数据时，如果key不存在，返回None
print(d.get('onee'))
