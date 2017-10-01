class Solution(object):
    def myAtoi(self,str):
        i=0
        x=0
        sign=0
        while i < len(str):
            if str[i]==' ':
                i=i+1
            else:
                break
        if i==len(str):
            return(0)
    
        if str[i]=='-':
            sign= -1
            i=i+1
        elif str[i]=='+':
            sign=1
            i=i+1
        else:
            sign=1


        while i < len(str):
            if 48<= ord(str[i])<=57:
                x=int(str[i])+x*10 
                i=i+1
            else:
                break
        if -2147483648>sign*x:
            return(-2147483648)
        if sign*x>2147483647:
            return(2147483647)
        return(sign*x)
