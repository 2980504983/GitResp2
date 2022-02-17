# 题目3：（字母识词）请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，
# 则继续判断第二个字母。

# 方法一
# 先判断是否是有两种可能的字母，如不是，判断字母与星期几的首字母相同，就打印星期几
# 如是，就在判断。这种方法代码显得比较臃肿,lower()方法是把输入字母变成小写，
# 这样就算输入大写的字母也能判断
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
           'saturday', 'sunday']
s3 = input('请输入第一个字母：')
for item in weekday:
    if s3.lower() == 't':
        s4 = input('你输入的字母有两种可能，请再输一个：')
        if s4.lower() == 'u':
            print(weekday[1:2])
            break
        else:
            print(weekday[3:4])
            break
    elif s3.lower() == 's':
        s5 = input('你输入的字母有两种可能，请再输一个：')
        if s5.lower() == 'u':
            print(weekday[6:5:-1])
            break
        else:
            print(weekday[5:4:-1])
            break
    if s3.lower() == item[0:1]:
        print(item)


# 方法二
# 如果输入t或s，就在让其输入第二个字母，在通过第二个字母来判断是星期几
# 这种方法通过将，相同首字母的的星期，通过第二个字母联系在一个字典中，在将该字典当成一个
# 集合与相同的首字母联系，并将它和其他不重复的星期，放在同一个字典中,这样当代码为重复星期的
# 首字母时就在让她输入第二个字母, 在通过首字母相同星期的字典找出是星期几
weekT = {'h': 'thursday', 'u': 'tuesday'}
weekS = {'a': 'saturday', 'u': 'sunday'}
week = {'t': weekT, 's': weekS, 'm': 'monday', 'w': 'wednesday',
        'f': 'friday'}
a = week[str(input('请输入第一位字母:')).lower()]
if a == weekT or a == weekS:
    print(a[str(input('请输入第二位字母:')).lower()])
else:
    print(a)
