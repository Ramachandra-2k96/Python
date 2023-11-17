def diff2(fname1, fname2):
    answers = []

    def diff1(fname1, fname2):
        difflines = []
        f1 = open(fname1, "r")
        f2 = open(fname2, "r")
        list1 = f1.readlines()
        list2 = f2.readlines()
        list3 = []
        list4 = []
        len1 = max(len(list1), len(list2))
        for i in range(0, len1, 1):
            line1 = list1[i].replace("\n", "")
            line2 = list2[i].replace("\n", "")
            if line1 != line2:
                difflines.append(i)
                list3.append(line1)
                list4.append(line2)
        return difflines, list3, list4

    result = diff1(fname1, fname2)
    difflines = result[0]
    list3 = result[1]
    list4 = result[2]
    for j in range(0, len(difflines), 1):
        lineno = difflines[j]
        list5 = list3[j].split(" ")
        list6 = list4[j].split(" ")
        len5 = max(len(list5), len(list6)) 
        count = 0
        line_diff = "line "+str(lineno) +" mismatch "
        for i in range(0, len5, 1):
            word1 = list5[i] if i < len(list5) else ""
            word2 = list6[i] if i < len(list6) else ""
            
            if word1 != word2:
                if count == 0:
                    line_diff += " word "+str(i)+" "+word1+" : "+word2 
                    count+=1 
                else:
                     line_diff += word1+"  "+word2    
                     
        answers.append(line_diff)

    return answers

fname1 = "file1.txt"
fname2 = "file2.txt"
result = diff2(fname1, fname2)
for item in result:
    print(item)
