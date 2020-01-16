import re
row="wbbwbbbw"
d=re.compile('wb*w')
nrow=""
over=""
for i in row:
    if len(nrow)!=4:
        nrow+=i
    else:
        print(d.findall(nrow))
        over=nrow
        nrow=""


#print(nrow)
#print(d.findall(row))
for i in d.findall(row):
    if i=='b':
        nrow+='w'
    elif i== '1':
        nrow+='w'
    else:
        nrow+=i
#print(nrow)
if nrow in row:
    print("yay")

else:
    print("nay")
#m = re.search('(<=abc)def','abcdef')
#print(m.group(0))
