def file_handel(file_path):
    f1= open(file_path,'r')
    f1.readline()
    name =[]
    age = []
    gender = []
    survived = []
    list1 =[]
    for f in f1:
        list1 = f.split(',')
        name.append(list1[4])
        gender.append(list1[5])
        survived.append(True if '1' == list1[1] else False)
        if not list1[6] =='':
            age.append(int(float(list1[6])))
        else:
            age.append(40)
    return (name,age,gender,survived)



scount,lcount = 0,0
name,age,gender,survived = file_handel('titanic.csv')
for s in survived:
    if s:
        scount += 1
    else:
        lcount += 1
   
        
print("The survivers ",scount, " and  they are :")
temp = []
children = []
male =[]
female = []
for n, a, g, s in zip(name, age, gender, survived): 
    if s and a<10 :
        temp =[s, n, g, a]
        children.append(temp)
    if s and a>=10 and g =='male':
        temp =[s, g, n, a]
        male.append(temp) 
    if s and a>=10 and g =='female':
        temp =[s, g, n, a]
        female.append(temp) 
        
print("children : ",len(children),"\n")        
print("Male : ",len(male),"\n")        
print("Female : ",len(female),"\n")        

children = []
male =[]
female = []
print("The Non-survivers ",lcount, " and  they are :")
for n, a, g, s in zip(name, age, gender, survived): 
    if (not s) and a<10 :
        temp =[s, n, g, a]
        children.append(temp)
    if (not s) and a>=10 and g =='male':
        temp =[s, g, n, a]
        male.append(temp) 
    if (not s) and a>=10 and g =='female':
        temp =[s, g, n, a]
        female.append(temp) 
        
print("children : ",len(children),"\n")        
print("Male : ",len(male),"\n")        
print("Female : ",len(female),"\n")        



