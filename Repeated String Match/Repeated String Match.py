class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i=0
        D=0
        D=-(-len(B)/len(A))
        C=A*D
        if B in C:
            return(D)
        C=C+A
        D=D+1
    
        if B in C:
            return(D)
        else:
            return (-1)
    