def create_website(college,fname):
    fname =fname
    college =college
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
    def create_content(fname):
        subjects =[]
        names = []
        file1 = open(fname,'r')
        lines = file1.readlines()
        list1 =[]
        for l in lines:
            list1 = l.split(':')
            subjects.append(list1[0])
            list2 = list1[1].replace('\n','').split(',')
            names.append(list2)
        return (subjects,names)
        
    subjects,names = create_content(fname)
    print(subjects)
    print(names)
    def create_dirs(list1,list2): 
        subjects = list1 
        names = list2 
        for s in subjects:
            os.makedirs(college+'/'+s,exist_ok=True)
        for j in range(0,5,1):
            len1 = len(names[j])
            for i in range(0,len1,1):
                os.makedirs(college+'/'+subjects[j]+'/'+names[j][i],exist_ok =True) 
    create_dirs(subjects,names)                 
