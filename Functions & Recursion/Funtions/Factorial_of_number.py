
#WAF to find the factorial of n.

def cal_fac(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

a = cal_fac(15)
print(a)