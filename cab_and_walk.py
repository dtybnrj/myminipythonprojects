x=input()
l=x.split()
N=int(l[0])
v1=int(l[1])
v2=int(l[2])
t1=v1/(1.414*N)
t2=v2/(2*N)
if t1>t2:
    print("Walk")
else:
    print("Cab")
