#!/usr/bin/python
# reference: https://www.johndcook.com/blog/2018/07/10/cayley-dickson/
import numpy as np

def conj(x):
    s1 = '_M_'
    k=0
    n = len(x)
    xstar = x
    for i in range(len(x)):
        xstar[i] = s1+x[i]
    xstar[0] =  x[0]
    return xstar

def CayleyDickson(x, y):
    n = len(x)
    s1 = '*'
    if n == 1:
        ss= (x[0]) + s1 + (y[0])
        return ss

    m = n // 2

    a, b = x[:m], x[m:]
    c, d = y[:m], y[m:]
    s1m = '_M_'
    s1p = '_p_'
    z  =  x
    ZZ=CayleyDickson(a, c)
    ZZ2=CayleyDickson(conj(d), b)
    ss=CayleyDickson(d, a) 
    ss1= CayleyDickson(b, conj(c))

    for i in range(len(ZZ)):
        z[i] = (ZZ[i] ) + s1m +  (ZZ2[i])
        z[m+i] =  (ss[i] ) + s1p + (ss1[i])
        return z


a = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
b = ['G0', 'G1', 'G2', 'G3', 'E4', 'E5', 'E6', 'E7']


c = CayleyDickson(a, b)

for i in range(len(c)):
    print(a[i])
    print(c[i])


