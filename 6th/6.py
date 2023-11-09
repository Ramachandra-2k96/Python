import os
s1= """<!DOCTYPE html>
<html>
<head>
    <title>Custom Video Player</title>
    <style>
       
    </style>
</head>
<body class="bg-gray-900 flex justify-center items-center h-screen">
   <h1>I am """ 
s2 ="""</h1>
</body>
</html>"""

def create_profile_page(f1):
    sub = []
    teacher = []
    lines = f1.readlines()
    for line in lines:
        line = line.replace('\n', '').split(':')
        sub.append(line[0])
        name =line[1].split(',')
        for i in name:
            os.makedirs(line[0]+'/'+i, exist_ok=True)

    for s in sub:
        for root, dirs, files in os.walk(s):
            for directory in dirs:
                subfolder_path = os.path.join(root, directory)
                with open(os.path.join(subfolder_path,directory+'.html'),'w') as new_f:
                    new_f.write(s1+directory+s2)
                    
                        
f1 = open("TeacherWebsite.txt", 'r')
create_profile_page(f1)