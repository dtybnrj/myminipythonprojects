n=input()
a=n.split(" ")
r=int(a[0])
c=int(a[1])
def binary_mat(mat):
    for i in range(r):
        for j in range(c):
            if (mat[i][j]==1 or mat[i][j]==0)==False:
                return False
    return True
if __name__=='__main__':
    mat=[[j for j in input().split()] for i in range(r)]
    if binary_mat(mat):
        print("YES",end="")
    else:
        print("NO",end="")