from exp import Val, Add

def paser(s: str):
    num=int(s)
    return Val(num)
e=paser("123")
print(e)

s="1+2"
pos=s.find('+')
print('pos',pos)

s1=s[0:pos]
s2=s[pos+1:]
print(s,s1,s2)

parse("1")
parse("1+2")
parse("1+2+3")



