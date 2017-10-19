def Match(A, B):
    i=0
    C=A
    D=0
    while len(C) <len(B):
        C=A+A
    C=C+A
    while i<len(C):
        if(i==len(C)-1):
            return(-1)
        j=0
        while (C[i+j]==B[j]):
            if(j==(len(B)-1)):
                D=-(-(i+j+1)/len(A))
                return(D)
            j=j+1

        i=i+1
A="abc"
B="cabca"
print (Match(A,B)) 