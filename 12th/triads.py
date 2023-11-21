def list_triad():
    import math
    triad=[]
    for i in range(1,20,1):
        for j in range(i+1,20,1):
            num1 = i**2
            num2 = j**2
            c = math.sqrt(num1+num2) 
            if c==int(c):
                triad.append([i,j,int(c)])
    return triad        
print(list_triad())   
