import itertools;s='wwwwooooggggrrrrbbbbyyyy';q=1
def z(r):
    w='';t=[];b=0;m=['R','R\'','R2','U','U\'','U2','F','F\'','F2']
    for x in itertools.product(m,repeat=r):
        for i in x:
            if i[0]==w:b=1
            w=i[0]
        if b==0:t.append(' '.join(x));w=''
        b=0
    return t
def R(c):
    r='080102110405060720091023131415121603001918212217';n=list(c)
    for i in range(24):n[i]=c[int(r[(2*i):(2*i)+2])]
    return ''.join(n)
def U(c):
    u='010203000809060712131011161714150405181920212223';n=list(c)
    for i in range(24):n[i]=c[int(u[(2*i):(2*i)+2])]
    return ''.join(n)
def F(c):
    f='000107042105062009101108120203151617181913142223';n=list(c)
    for i in range(24):n[i]=c[int(f[(2*i):(2*i)+2])]
    return ''.join(n)
def y(c,e):
    c=c+e
    for x in e.split():
        if x=='R':c=R(c)
        elif x=='R\'':c=R(R(R(c)))
        elif x=='R2':c=R(R(c))
        elif x=='U':c=U(c)
        elif x=='U\'':c=U(U(U(c)))
        elif x=='U2':c=U(U(c))
        elif x=='F':c=F(c)
        elif x=='F\'':c=F(F(F(c)))
        else:c=F(F(c))
    return c
def w(v):
    n = ''
    for i in v[24:].split()[::-1]:
        if i=='R':n=n+'R\' '
        elif i=='U':n=n+'U\' '
        elif i=='F':n=n+'F\' '
        elif i=='R\'':n=n+'R '
        elif i=='U\'':n=n+'U '
        elif i=='F\'':n=n+'F '
        else:n=n+i+' '
    return n
def r(s):
    s = s.split()
    for x in range(6):
        try:
            if s[x][0] == s[x+1][0]:
                a = s[x]; b = s[x+1];del s[x+1]
                if a=='R':
                    if b=='R':s[x]='R2'
                    elif b=='R\'':del s[x]
                    else:s[x]='R\''
                elif a=='U':
                    if b=='U':s[x]='U2'
                    elif b=='U\'':del s[x]
                    else:s[x]='U\''
                elif a=='F':
                    if b=='F':s[x]='F2'
                    elif b=='F\'':del s[x]
                    else:s[x]='F\''
                elif a=='R\'':
                    if b=='R':del s[x]
                    elif b=='R\'':s[x]='R2'
                    else:s[x]='R'
                elif a=='U\'':
                    if b=='U2':s[x]='U'
                    elif b=='U':del s[x]
                    else:s[x]='U2'
                elif a=='F\'':
                    if b=='F\'':s[x]='F2'
                    elif b=='F2':s[x]='F'
                    else:del s[x]
                elif a=='R2':
                    if b=='R':s[x]='R\''
                    elif b=='R2':del s[x]
                    else:s[x]='R'
                elif a=='U2':
                    if b=='U':s[x]='U\''
                    elif b=='U2':del s[x]
                    else:s[x]='U'
                else:
                    if b=='F\'':s[x]='F'
                    elif b=='F2':del s[x]
                    else:s[x]='F'
        except:pass
    return ' '.join(s)
c=y(s, input(': '))
while q!=0:
    f=[];g=[];o=[]
    for l in z(q):f.append(y(c[:24], l));g.append(y(s, l))
    for u in f:
        for v in g:
            if u[:24]==v[:24]:
                k=r(u[24:]+' '+w(v))
                if k not in o:print(k);o.append(k);q=-1
    q+=1
