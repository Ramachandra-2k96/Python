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

def survivers(name,age,gender,survived):
    children, male, female =[],[],[]
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
    return (children,male,female)

def Non_survivers(name,age,gender,survived):
    children, male, female =[],[],[]
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
    return [children,male,female]


name,age,gender,survived = file_handel('titanic.csv')
temp = []
children, male, female = survivers(name,age,gender,survived)
print("The total survivers = ",len(children)+len(male)+len(female), " and  they are :")
print("children : ",len(children))        
print("Male : ",len(male))        
print("Female : ",len(female))        

children, male, female = Non_survivers(name,age,gender,survived)
print("\nThe total Non-survivers = ",len(children)+len(male)+len(female), " and  they are :")
print("children : ",len(children))        
print("Male : ",len(male))        
print("Female : ",len(female))        



