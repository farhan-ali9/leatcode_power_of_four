#first soltion
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0


#second solution
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        while n%4==0: #5!=0
            n=n//4
        return n==1
#third solution 
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        elif n==1:
            return True
        elif n%4==0:
            return True
        else:
            return False

                
