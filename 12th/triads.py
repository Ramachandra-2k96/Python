import math
triad1 =[]
triad2 =[]
triad3 =[]
triad =[]
for i in range(1,20,1):
    for j in range(i+1,20,1):
        num1 = i**2
        num2 = j**2
        c = math.sqrt(num1+num2) 
        if c==int(c):
            triad1.append(i)
            triad2.append(j)
            triad3.append(int(c))
            
for (i,j,k) in zip(triad1,triad2,triad3):
    triad.append([i,j,k])
print(triad)   

