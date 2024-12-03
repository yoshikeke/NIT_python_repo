n = int(input())
def isPrime(x):
    if x != 1:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    else :
        return False
    
prime = []
i = 2
while len(prime)<100:
    if isPrime(i):
        prime.append(i)
    i += 1

print(prime[n-1])