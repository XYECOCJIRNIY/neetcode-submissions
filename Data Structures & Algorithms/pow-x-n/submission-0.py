class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        flag = False
        
        if n == 0:
            return 1
        
        elif n < 0:
            flag = True
            n = abs(n)

        while n > 0:
            if n % 2 == 1:
                result *= x
            
            x *= x
            n //= 2

        if flag:
            result = 1 / result

        return result


        

        