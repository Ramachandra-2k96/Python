def cal31():
    import calendar as cl
    months31 = [1,3,5,7,8,10,12]
    list1 = []
    for i in months31:
        #print(cl.calendar(2023))#whole calender
        list1.append(cl.month(2023,i))#1 month
    return list1
        
def cal30():
    import calendar as cl
    list1=[]
    months30 = [4,6,9,11]
    for i in months30:
        list1.append(cl.month(2023,i))#1 month
    return list1

def cal28():
    import calendar as cl
    list1=[]
    months28 = [1]
    for i in months28:
        list1.append(cl.month(2023,i))#1 month
    return list1
        
def caln(days):
    f = open('caln.txt','w') 
    cal =[]
    if days == 31:
        cal = cal31()
    elif days==30:
        cal = cal30()
    else:
        cal = cal28()
    for c in cal:
        f.write(c)
        
n1 = int(input("Enter number of days : "))
caln(31)
