def isPrime(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
if isPrime(5):
    print("isPrime!")
prime_nums=[]
bignum=input("get prime numbers less than:")
for j in range(2,int(bignum)):
    if isPrime(j):
        prime_nums.append(j)
print("primes less than",bignum,prime_nums)

