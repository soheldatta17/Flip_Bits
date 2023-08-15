class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        max=0
        zero=0
        one=0
        for i in a:
            if (i==0):
                zero+=1
            else:
                zero-=1
                one+=1
                if zero<0:
                    zero=0
            #Max check
            if zero>max:
                max=zero
        return max+one