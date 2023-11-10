import new as n
import shutil
college = "SMVITM"
print(n.website_creation(college,"TeacherWebsite.txt"))
import time 
shutil.make_archive('SMVITM', 'zip' , college)
time.sleep(5)
shutil.rmtree(college)