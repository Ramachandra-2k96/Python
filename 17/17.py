import csv
state = input("Enter state-code :").upper().strip()
maps ={}
with open("Holidays_2024.csv", 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        maps[row[0]] = [row[1], row[2], row[3].replace("\n", " ").replace('&',',')]
for d,value in maps.items():
    if state in value[2] and "except" not in value[2]:
        print(d,value[0],", Occasion :",value[1])