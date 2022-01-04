import itertools
def z(r):
    w=''; t=[];b=0;m=['R','R\'','R2','U','U\'','U2','F','F\'','F2']
    for x in itertools.product(m,repeat=r):
        for i in x:
            if i[0]==w:
                b=1
            w=i[0]
        if b==0:
            t.append(' '.join(x));w=''
        b=0
    return t
def R(c):
    r='080102110405060720091023131415121603001918212217';n=list(c)
    for i in range(24):
        n[i] = c[int(r[(2*i):(2*i)+2])]
    return ''.join(n)
def U(c):
    u='010203000809060712131011161714150405181920212223';n=list(c)
    for i in range(24):
        n[i] = c[int(u[(2*i):(2*i)+2])]
    return ''.join(n)
def F(c):
    f = '000107042105062009101108120203151617181913142223';n=list(c)
    for i in range(24):
        n[i] = c[int(f[(2*i):(2*i)+2])]
    return ''.join(n)
def y(c,e):
    c=c+e
    for x in e.split():
        if x=='R':
            c=R(c)
        elif x=='R\'':
            c=R(R(R(c)))
        elif x=='R2':
            c=R(R(c))
        elif x=='U':
            c=U(c)
        elif x=='U\'':
            c=U(U(U(c)))
        elif x=='U2':
            c=U(U(c))
        elif x=='F':
            c=F(c)
        elif x=='F\'':
            c=F(F(F(c)))
        else:
            c=F(F(c))
    return c
s='wwwwooooggggrrrrbbbbyyyy';q=1
c=y(s, input(': '))
while q!=0:
    f=[];g=[]
    for l in z(q):
        f.append(y(c[:24], l))
        g.append(y(s, l))
    for u in f:
        for v in g:
            if u[:24]==v[:24]:
                q=-1
    q+=1
