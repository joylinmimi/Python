class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=x*(-1)
            y=0
            while x>0:
                y=y*10+(x%10)
                x=x/10
            if y> 2147483647:
                return(0)
            else:
                return(-y)
        else:    
            y=0
            while x>0:
                y=y*10+(x%10)
                x=x/10
            if y> 2147483647:
                return(0)
            else:
                return(y)
        
