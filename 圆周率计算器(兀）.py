pi=0
N=100
for i in range(N):
    pi+=1/pow(16,i)*(4/(8*i+1)-\
        2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print(pi)
