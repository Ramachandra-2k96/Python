def perm3(word3):
    word3=word3
    list3=[]
    s1=word3[0:1]
    s2=word3[1:2]
    s3=word3[2:3]
    list3.append(s1+s2+s3)
    list3.append(s1+s3+s2)
    list3.append(s2+s1+s3)
    list3.append(s2+s3+s1)
    list3.append(s3+s1+s2)
    list3.append(s3+s2+s1)
    return list3


def perm4(word4):
    word4=word4
    list4=[]
    s1=word4[0:1]
    s2=word4[1:2]
    s3=word4[2:3]
    s4=word4[3:4]
    part1=s1
    part2=s2+s3+s4
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    part1=s2
    part2=s1+s3+s4
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    part1=s3
    part2=s1+s2+s4
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    part1=s4
    part2=s1+s2+s3
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    return list4


def perm5(word5):
    word5=word5
    list5=[]
    s1=word5[0:1]
    s2=word5[1:2]
    s3=word5[2:3]
    s4=word5[3:4]
    s5=word5[4:5]
    part1=s1
    part2=s2+s3+s4+s5
    result=perm4(part2)
    for i in result:
        list5.append(part1+i)
    part1=s2
    part2=s1+s3+s4+s5
    result=perm4(part2)
    for i in result:
        list5.append(part1+i)
    part1=s3
    part2=s1+s2+s4+s5
    result=perm4(part2)
    for i in result:
        list5.append(part1+i)
    part1=s4
    part2=s1+s2+s3+s5
    result=perm4(part2)
    for i in result:
        list5.append(part1+i)
    part1=s5
    part2=s1+s2+s3+s4
    result=perm4(part2)    
    for i in result:
        list5.append(part1+i)
    return list5

def perm6(word6):
    word6=word6
    list6=[]
    part1=word6[0]
    part2=word6[1:6]
    result=perm5(part2)   
    for i in result:
        list6.append(part1+i)
    part1=word6[1]
    part2=word6[0]+word6[2:6]
    result=perm5(part2)   
    for i in result:
        list6.append(part1+i)
    part1=word6[2]
    part2=word6[0:2]+word6[3:6]
    result=perm5(part2)
    for i in result:
        list6.append(part1+i)
    part1=word6[3]
    part2=word6[0:3]+word6[4:6]
    result=perm5(part2)
    for i in result:
        list6.append(part1+i)
    part1=word6[4]
    part2=word6[0:4]+word6[5:6]
    result=perm5(part2)
    for i in result:
        list6.append(part1+i)
    part1=word6[5]
    part2=word6[0:5]+word6[6:6]
    result=perm5(part2)
    for i in result:
        list6.append(part1+i)        
    return list6


def perm7(word7):
    word7=word7
    list7=[]
    part1=word7[0]
    part2=word7[1:7]
    result=perm6(part2)   
    for i in result:
        list7.append(part1+i)
    part1=word7[1]
    part2=word7[0]+word7[2:7]
    result=perm6(part2)   
    for i in result:
        list7.append(part1+i)
    part1=word7[2]
    part2=word7[0:2]+word7[3:7]
    result=perm6(part2)
    for i in result:
        list7.append(part1+i)
    part1=word7[3]
    part2=word7[0:3]+word7[4:7]
    result=perm6(part2)
    for i in result:
        list7.append(part1+i)
    part1=word7[4]
    part2=word7[0:4]+word7[5:7]
    result=perm6(part2)
    for i in result:
        list7.append(part1+i)
    part1=word7[5]
    part2=word7[0:5]+word7[6:7]
    result=perm6(part2)
    for i in result:
        list7.append(part1+i)
    part1=word7[6]
    part2=word7[0:6]+word7[7:7]
    result=perm6(part2)
    for i in result:
        list7.append(part1+i)        
    return list7

def perm8(word8):
    word8=word8
    list8=[]
    part1=word8[0]
    part2=word8[1:8]
    result=perm7(part2)   
    for i in result:
        list8.append(part1+i)
    part1=word8[1]
    part2=word8[0]+word8[2:8]
    result=perm7(part2)   
    for i in result:
        list8.append(part1+i)
    part1=word8[2]
    part2=word8[0:2]+word8[3:8]
    result=perm7(part2)
    for i in result:
        list8.append(part1+i)
    part1=word8[3]
    part2=word8[0:3]+word8[4:8]
    result=perm7(part2)
    for i in result:
        list8.append(part1+i)
    part1=word8[4]
    part2=word8[0:4]+word8[5:8]
    result=perm7(part2)
    for i in result:
        list8.append(part1+i)
    part1=word8[5]
    part2=word8[0:5]+word8[6:8]
    result=perm7(part2)
    for i in result:
        list8.append(part1+i)
    part1=word8[6]
    part2=word8[0:6]+word8[7:8]
    result=perm7(part2)
    for i in result:
        list8.append(part1+i)
    part1=word8[7]
    part2=word8[0:7]+word8[8:8]
    result=perm7(part2)
    for i in result:
        list8.append(part1+i)        
    return list8


def perm9(word9):
    word9=word9
    list9=[]
    part1=word9[0]
    part2=word9[1:9]
    result=perm8(part2)   
    for i in result:
        list9.append(part1+i)
    part1=word9[1]
    part2=word9[0]+word9[2:9]
    result=perm8(part2)   
    for i in result:
        list9.append(part1+i)
    part1=word9[2]
    part2=word9[0:2]+word9[3:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)
    part1=word9[3]
    part2=word9[0:3]+word9[4:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)
    part1=word9[4]
    part2=word9[0:4]+word9[5:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)
    part1=word9[5]
    part2=word9[0:5]+word9[6:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)
    part1=word9[6]
    part2=word9[0:6]+word9[7:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)
    part1=word9[7]
    part2=word9[0:7]+word9[8:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)
    part1=word9[8]
    part2=word9[0:8]+word9[9:9]
    result=perm8(part2)
    for i in result:
        list9.append(part1+i)        
    return list9
