def readlines_and_compare(file1,file2):
    with open(file1, 'r') as file1:
        sentences_file1 = file1.read().splitlines()
    with open(file2, 'r') as file2:
        sentences_file2 = file2.read().splitlines()
    fault_lines =[]
    for i, (line1, line2) in enumerate(zip(sentences_file1, sentences_file2), start=1):
        if line1 != line2:
            fault_lines.append(i)
    return fault_lines

def compare_words(file1,file2):
    with open(file1, 'r') as file1:
        sentences_file1 = file1.read().splitlines()
    with open(file2, 'r') as file2:
        sentences_file2 = file2.read().splitlines()
    fault_words =[]
    for i, (line1, line2) in enumerate(zip(sentences_file1, sentences_file2), start=1):
        words1 =line1.split(" ")
        words2 =line2.split(" ")
        for (word1,word2) in zip(words1,words2):
            if word1!=word2:
                fault_words.append(line1+" : "+word1)
                fault_words.append(line2+" : "+word2)
    return fault_words 

print(readlines_and_compare('file1.txt',"file2.txt"))
print(compare_words('file1.txt',"file2.txt"))