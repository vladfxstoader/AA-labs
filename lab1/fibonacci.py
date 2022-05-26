#3.1
def fibonacci(i): # O(2^n)
    if i==1:
        return 1
    elif i==2:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)

#3.2
dict_fib={1:1,2:1}
def fibonacci2(n): # O(n) timp, O(n) spatiu
    if n in dict_fib.keys():
        return dict_fib[n]
    else:
        dict_fib[n]=fibonacci2(n-1)+fibonacci2(n-2)
        return dict_fib[n]

#3.3
def fibonacci3(n):  #O(n)
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        a=1
        b=1
        c=a+b
        index = 2
        while index<n-1:
            a=b
            b=c
            c=a+b
            index=index+1
        return c
n=int(input("Introduceti n:"))
print(fibonacci3(n))