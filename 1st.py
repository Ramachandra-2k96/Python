#Rule 4 is import here
import mod_rule4 as mr4
# all the strings are included here
import strings as S  


#all the variables required                                                
alpha =[]
word_done = []
man_sum = 0
Computer_sum = 0 
last_word = ""
timeout = 30


# creating list fo alphabets here
for i in range(97,97+26,1):                      
    alpha.append(chr(i))   

# with file name opening a file and making the nested list of words based on the first letter
def transform1(file):                           
        f1 = open(file,'r')
        list1 = f1.read().split('\n')
        list2 = []
        for j in range(0,26,1):
            templist = []
            for i in range(0,len(list1),1):
                if list1[i][0] == alpha[j]:
                    templist.append (list1[i])
            list2.append(templist) 
        return list2


#updating the list and choosing best word for computer
def transform2(word, list1):
    lastchar = word[-1]
    pos = alpha.index(lastchar)
    templist = list1[pos]
    for word1 in word_done:
        if word1 in templist:
            templist.remove(word1)
    if templist:
        max_size_word = templist[0]
        for new_word in templist:
             if len(new_word) > len(max_size_word) and len(new_word) >len(word):
                 max_size_word = new_word
        return max_size_word 
    else:
        return None



list1 = transform1('words.txt')
for i in range(100):
    dif,input1 = mr4.rule4(S.s1,timeout)                 #Rule 4 satisfied
    if dif >timeout:
        print('You took', dif-timeout, ' seconds extra')
        print(S.s3)
        break
    if input1 in word_done:                              # Rule 3 satisfied
        print(S.s2, "\n", S.s4, "\n", S.s3)
        print(S.s5, man_sum, S.s6, Computer_sum)
        break
    if last_word == "" or last_word[-1] == input1[0]:     #Rule 2 satisfied
        word_done.append(input1)
        man_sum += len(input1)
        last_word = transform2(input1, list1)
        if last_word is None:
            print(S.s7)
            print(S.s5, man_sum, S.s6, Computer_sum)
            break
        else:
            word_done.append(last_word)
            Computer_sum += len(last_word)
            print(S.s8 + last_word + "\n")
            print(S.s5, man_sum, S.s6, Computer_sum, "\n")
    else:
        print(S.s9, "\n", S.s3)
        print(S.s5, man_sum, S.s6, Computer_sum)
        break 

if man_sum <= Computer_sum:
    print("You Lost with ", Computer_sum-man_sum, S.s10)
else:
    print("YOU WIN !!! with ", man_sum-Computer_sum, S.s10)

