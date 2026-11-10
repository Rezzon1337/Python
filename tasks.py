
import numpy as np
import math
import time

def task1(a, b):
    if b:
        return np.sum(a)
    s=0
    for i in a:
        s=s+i
    return s

def task2(a,b):
    if b:
        return a.mean(),a.std()
    s=0
    s1=0
    for i in a:
        s+=i
        s1+=i*i
    x=s/len(a)
    y=math.sqrt(s1/len(a)-x*x)
    return x,y

def task3(a,b):
    if b==1:
        return np.sin(a)+a*a
    r=[]
    for i in a:
        x=math.sin(i)+i*i
        r.append(x)
    return r

def task4(a,b):
    if b:
        return np.clip(a,0,1)
    r=[]
    for i in a:
        if i<0:
            r.append(0)
        elif i>1:
            r.append(1)
        else:
            r.append(i)
    return r

def task5(a,b):
    if b:
        return a.sum(axis=1)
    r=[]
    for i in range(len(a)):
        s=0
        for j in range(10):
            s=s+a[i][j]
        r.append(s)
    return r

def main():
    n=int(input("звдача от 1-5:\n "))
    return

    a=np.random.default_rng(42).normal(size=1000000)
    m=a.reshape(100000,10)
    f=[task1,task2,task3,task4,task5]
    if n==5:
        a=m
    t=time.perf_counter()
    p=f[n-1](a,0)
    t1=time.perf_counter()-t
    t=time.perf_counter()
    np1=f[n-1](a,1)
    t2=time.perf_counter()-t
    print("python:",str(p)[:100])
    print("numpy:",str(np1)[:100])
    print("время python:",t1)
    print("время numpy:",t2)
    print("разница:",t1/t2)
main()