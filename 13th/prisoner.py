from datetime import datetime , timedelta
#we Will get the same output using this method
def Prison_problem1(count):
    i=1
    prison = ['C']*count
    while(i<=count):
        j=i**0.5
        if int(j) ==j:
            prison[i-1]="O"
        i=i+1    
    return prison

#Main logic :
def Prison_problem(count):
    prison =["C"]*count
    # first condition :open all the gates
    # for i in range(0,count):
    #     prison[i] ="O"
    # Second condition : Close all 2 alternate gates
    # for i in range(1,count,2):
    #     prison[i]="C" 
    # next condition continue closE THE GATE if it is open and open the gate it its closed for alternate gates 3,4,5.....
    for j in range(0,count):
        for i in range(j,count,j+1): 
            if prison[i]=="C":
                prison[i]="O" 
            else:
                prison[i]="C"
    return prison 

def mail_pm():
    result = Prison_problem(100)
    lucky,unlucky=[],[]
    for i,r in enumerate(result,start=1):
        if r == 'O':
            lucky.append(str(i))
        else:
            unlucky.append(str(i))
    with open("Lucky.txt","w")as luck:
        luck.write("Dear Prime Minister,\n   I am writing to inform you about a list of lucky prisoners who have been granted early release.\n")  
        luck.write(f"   Their release date is scheduled for {datetime.now().date()}\n")  
        luck.write(f"   The identification numbers of the lucky prisoners are : \n   {','.join(lucky)}\n")
        luck.write("Thank you")    
    return unlucky

def mail_jailer(unlucky):
    with open("Unlucky.txt","w")as luck:
        luck.write("Dear Jailer,\n   I am writing to inform you about a list of unlucky prisoners who have been granted release.\n")  
        luck.write(f"   Their release date is scheduled for {datetime.now().date()+timedelta(weeks=4)}\n")  
        luck.write(f"   The identification numbers of the prisoners are : \n   {','.join(unlucky)}\n")
        luck.write("Thank you")
    print("mail sent")
    
un_lucky = mail_pm()
mail_jailer(un_lucky)  

    