import decimal
def getsigma(k):
    if k==-1:
        return 0
    current=decimal.Decimal(1/(16**k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)))
    #return 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/8*k+6)+getsigma(k-1)
    return getsigma(k-1)+current
pi=decimal.Decimal("0.0")
for k in range(11114):
    pi+=decimal.Decimal(1/(16**k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)))
    #   1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)
print(pi)
print(getsigma(996))
