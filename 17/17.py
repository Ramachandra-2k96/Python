import csv
list1 =[]
with open("Holidays_2024.csv", 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list1 .append([row[0],row[1], row[2], row[3].replace("\n", " ").replace('&',',')])
for l in list1:
    if "KA" in l[3]:
        if "except" not in l[3]:
            print(l[0],l[1],", Occasion : ",l[2])
    elif "except" in l[3]:
        if "KA" not in l[3]:
            print(l[0],l[1],", Occasion : ",l[2])
    elif "National" in l[3]:
        print(l[0],l[1],", Occasion : ",l[2])