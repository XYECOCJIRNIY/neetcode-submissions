class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        negative = False
        
        if n < 0:
            negative = True
            n = abs(n)

        while n > 0:
            if n % 2 == 1:
                result *= x
            
            x *= x
            n //= 2

        if negative:
            result = 1 / result

        return result


        

        