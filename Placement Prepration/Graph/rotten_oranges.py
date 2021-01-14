def rotOranges(mat,n,m):
    rtn=[]
    frs=[]
    mx=[]
    for i in range(n):
        mx.append([])
        for j in range(m):
            mx[i].append([])
            v=mat[i][j]
            mx[i][j]=v
            if v==2:
                rtn.append((i,j))
            elif v==1:
                frs.append((i,j))
    
    vstd=[]
    
    def adj(cn,mx,n,m):
        al=[]
        i=cn[0]
        j=cn[1]
        pal=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for e in pal:
            if 0<=e[0]<n and 0<=e[1]<m:
                if mx[e[0]][e[1]]==1:
                    al.append(e)
        return al
        
    def rot(mx,r,fr,n,m):
        vstd=[]
        rotn=r
        c=0
        while rotn:
            c+=1
            nxtrtn=[]
            for e in rotn:
                vstd.append(e)
                for f in adj(e,mx,n,m):
                    mx[f[0]][f[1]]=2
                    nxtrtn.append(f)
            
            rotn=nxtrtn
        if len(vstd)==(len(r)+len(fr)):
            return c-1
        else:
            return -1
            
    return rot(mx,rtn,frs,n,m)

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        
        rc = input('Enter the number of row and column:- ').split() #row and column
        r = int(rc[0])    
        c = int(rc[1])
        l = list(map(int, input('Enter the elements of the graph:- ').strip().split(' ')))
        
        mat=[]
        for i in range(r):
            mat.append([])
            for j in range(c):
                mat[i].append([])
                mat[i][j]=l.pop()
                
        print(rotOranges(mat,r,c))