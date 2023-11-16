import mod_create_website as mw
import os
college ="SMVITM"
os.makedirs(college,exist_ok=True)
          
mw.create_website(college,'TeacherWebsite.txt')
for root, dirs, files in os.walk(college):
    if not dirs:
        dir_name = os.path.basename(root)
        with open(os.path.join(root, dir_name + '.html'), 'w') as file1:
                file1.write("<h1>hello There" + " I am " + dir_name + "</h1>")
#mw.create_website('StudentWebsite.txt')