import mod_rule4 as mr4
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word_done = []
man_sum = 0
Computer_sum = 0 


    
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



def transform2(word, list1):
    lastchar = word[-1]
    pos = alpha.index(lastchar)
    templist = list1[pos]
    for word1 in word_done:
        if word1 in templist:
            templist.remove(word1)
    if templist:
        return templist[0]  
    else:
        return None


last_word = ""
timeout = 10
s1 = "You  "
list1 = transform1('C:/Users/ramac/Downloads/words.txt')
for i in range(100):
    dif,input1 = mr4.rule4(s1,timeout) #Rule 4 satisfied
    if dif >timeout:
        print('You took',dif-timeout,' seconds extra')
        print('YOU LOOSE')
        break
    if input1 in word_done: # Rule 3 satisfied
        print("This word has already been used,")
        print("Game Finished")
        print('YOU LOOSE')
        print(" Your score :",man_sum,"\t Computer score : ",Computer_sum)
        break
    if last_word =="" or last_word[-1] == input1[0]: #Rule 2 satisfied
        word_done.append(input1)
        man_sum+=len(input1)
        last_word = transform2(input1, list1)
        if last_word is None:
            print("No available word found, YOU WIN !!!")
            print(" Your score :",man_sum,"\t Computer score : ",Computer_sum)
            break
        else:
            word_done.append(last_word)
            Computer_sum += len(last_word)
            print("Computer : "+last_word+"\n")
            print(" Your score :",man_sum,"\t Computer score : ",Computer_sum)
    else:
        print("Last Letter and Your First letter mismatch ")
        print("You LOOSE ")
        print(" Your score :",man_sum,"\t Computer score : ",Computer_sum)
        break 

if man_sum <= Computer_sum:
    print("You Lost with ",Computer_sum-man_sum," Points")
else:
    print("YOU WIN !!! with ",man_sum-Computer_sum," Points")

