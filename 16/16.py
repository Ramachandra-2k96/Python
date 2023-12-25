def perm3(str1):
    s1=str1[0]
    s2=str1[1]
    s3=str1[2]
    list1=[]
    list1.append(s1+s2+s3)
    list1.append(s1+s3+s2)
    list1.append(s2+s1+s3)
    list1.append(s2+s3+s1)
    list1.append(s3+s1+s2)
    list1.append(str1[::-1])
    return list1

def perm4(str1):
    list1 = []
    s1=str1[0]
    s2=str1[1:4]
    result = perm3(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[1]
    s2=str1[0]+str1[2:4]
    result = perm3(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[2]
    s2=str1[0:2]+str1[3:4]
    result = perm3(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[3]
    s2=str1[0:3]
    result = perm3(s2)
    for r in result:
        list1.append(s1+r)
    return list1

def perm5(str1):
    list1 = []
    s1=str1[0]
    s2=str1[1:5]
    result = perm4(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[1]
    s2=str1[0]+str1[2:5]
    result = perm4(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[2]
    s2=str1[0:2]+str1[3:5]
    result = perm4(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[3]
    s2=str1[0:3]+str1[4:5]
    result = perm4(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[4]
    s2=str1[0:4]
    result = perm4(s2)
    for r in result:
        list1.append(s1+r)
    return list1

def perm6(str1):
    list1 = []
    s1=str1[0]
    s2=str1[1:6]
    result = perm5(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[1]
    s2=str1[0]+str1[2:6]
    result = perm5(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[2]
    s2=str1[0:2]+str1[3:6]
    result = perm5(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[3]
    s2=str1[0:3]+str1[4:6]
    result = perm5(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[4]
    s2=str1[0:4]+str1[5:6]
    result = perm5(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[5]
    s2=str1[0:5]
    result = perm5(s2)
    for r in result:
        list1.append(s1+r)
    return list1

def perm7(str1):
    list1 = []
    s1=str1[0]
    s2=str1[1:7]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[1]
    s2=str1[0]+str1[2:7]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[2]
    s2=str1[0:2]+str1[3:7]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[3]
    s2=str1[0:3]+str1[4:7]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[4]
    s2=str1[0:4]+str1[5:7]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[5]
    s2=str1[0:5]+str1[6:7]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[6]
    s2=str1[0:6]
    result = perm6(s2)
    for r in result:
        list1.append(s1+r)
    return list1

def perm8(str1):
    list1 = []
    s1=str1[0]
    s2=str1[1:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[1]
    s2=str1[0]+str1[2:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[2]
    s2=str1[0:2]+str1[3:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[3]
    s2=str1[0:3]+str1[4:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[4]
    s2=str1[0:4]+str1[5:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[5]
    s2=str1[0:5]+str1[6:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[6]
    s2=str1[0:6]+str1[7:8]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[7]
    s2=str1[0:7]
    result = perm7(s2)
    for r in result:
        list1.append(s1+r)
    return list1

def perm9(str1):
    list1 = []
    s1=str1[0]
    s2=str1[1:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[1]
    s2=str1[0]+str1[2:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[2]
    s2=str1[0:2]+str1[3:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[3]
    s2=str1[0:3]+str1[4:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[4]
    s2=str1[0:4]+str1[5:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[5]
    s2=str1[0:5]+str1[6:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[6]
    s2=str1[0:6]+str1[7:9]
    result = perm9(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[7]
    s2=str1[0:7]+str1[8:9]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    s1=str1[8]
    s2=str1[0:8]
    result = perm8(s2)
    for r in result:
        list1.append(s1+r)
    return list1

input1 = input(" Enter a string to write permutation ").strip()
if len(input1) == 3:
    print(perm3(input1))
elif len(input1) == 4:
    print(perm4(input1))
elif len(input1) == 5:
    print(perm5(input1))
elif len(input1) == 6:
    print(perm6(input1))
elif len(input1) == 7:
    print(perm7(input1))
elif len(input1) == 8:
    print(perm8(input1))
elif len(input1) == 9:
    print(perm9(input1))
else:
    print(" Out of range ")