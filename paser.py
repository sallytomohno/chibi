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

def parse(s:str):
    pos=s.find('+')
    if pos==-1:
        num=int(s)
        return Val(num)
    else:
        s1=s[0:pos]
        s2=s[pos+1:]
        return Add(Val(int(s1)),Val(int(s2)))

e=parse("123+456+789")
print(e)
