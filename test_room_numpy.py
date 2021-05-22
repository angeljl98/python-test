import numpy as np
a=np.array([1,2,3])
b=np.array([3,2,1])
print(a+b)
print(any(a==b)) #ve si alguno es True
print(all(a==b)) #ve si todos son True

ts=[-8,8,17,15,45,-9,8] #problemas de las temperaturas
ts_len=len(ts)
c=np.zeros((4,ts_len))
for i in range(0,ts_len):
    c[0,i]=ts[i]
    c[1,i]=abs(ts[i])
    c[2,i]=i+1
d=min(c[1])
#Pass11$Ang
for i in range(0,ts_len):
    if abs(ts[i])==abs(d):
        c[3,i]=ts[i]
d=max(c[3])
print(c)
#c[(2,7)]=9
print(d)
