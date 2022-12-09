import numpy as np
n = np.random.randint(low=-1000,high=1001,size=1000)
n=list(n)
taptin = input("tap tin can nhap:")
tam=[]
for i in range(10):
    tam.append(i)
a=open(taptin,"w")
for i in range(100):
    for j in range(10):
        tam[j]=str(n[10*i+j])
    a.write(','.join(tam)+"\n")
a.close()
with open(taptin,"r") as a:
    print(a.read())

