s='aaa'
c=0
a=[]
l=len(s)
for i in s:
    if i not in a:
        a.append(i)
        a.sort()
if(len(a)==1 or l==2):
    print('IMPOSSIBLE')
else:
    if(l%2==1):
        b=l//2
        a.remove(s[b])
        d=list(s)
        d[b]=a[0]
        a.remove(d[b])
        if(a==[]):
            d[b+1]=s[b]
        else:
            if(s[b]<=a[0]):
                d[b+1]=s[b]
            else:
                d[b+1]=a[0]
        p="".join(d)
    else:
        b=l//2-1
        a.remove(s[b])
        d=list(s)
        d[b]=a[0]
        p="".join(d)
    print(p)