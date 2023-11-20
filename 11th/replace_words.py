#Simple replace logic it will not work if template is different
#But the user can use variables like $names as many times as he can in template
def replace_placeholders(template, salutation, name, amount, date):
    template = template.replace("$1salutation", salutation)
    template = template.replace("$2name", name)
    template = template.replace("$3amount", str(amount))
    template = template.replace("$4date", date)
    return template
def readfile(file):
    with open(file,'r')as f:
        list1 = f.read().split('\n')
    return list1
def read_template(file):
    string = ""
    with open(file,'r')as f:
        string = string + f.read().replace("\n","")
    return string
def write_file(list1):
    with open("output.txt",'w')as f:
        for l in list1:
            f.writelines(l + '\n')

main = readfile("list1.txt")
template = read_template("template.txt")
final_result =[]
for m in main:
    temp = m.split(', ')
    final_result.append(replace_placeholders(template,temp[0],temp[1],temp[2],temp[3]))

write_file(final_result)