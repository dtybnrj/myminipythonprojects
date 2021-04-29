def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]

        # Returns true if mat[N][N] is symmetric, else false
def isSymmetric(mat, N):

    tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True
n=int(input())
mat=[[j for j in input().split()] for i in range(n)]
if (isSymmetric(mat,n)):
    print("YES",end="")
else:
    print("NO",end="")