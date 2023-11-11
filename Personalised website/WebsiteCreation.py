import mod_create_website as mcw
import shutil
import time 
import mod_string_es as mes
import mod_string_en as men
import mod_string_de as mde
lang ="en"
if lang=="de": 
    s1,s2,s3,s4 = mde.strings()
elif lang=="es":
    s1,s2,s3,s4 = mes.strings()
else:
    s1,s2,s3,s4 = men.strings()

def time1():
    import datetime as dt
    today =dt.datetime.now()
    y1= str(today.year)
    m1=str(today.month).zfill(2)
    d1 = str(today.day).zfill(2)
    h1= str(today.hour).zfill(2)
    m2= str(today.minute).zfill(2)
    s2 = str(today.second).zfill(2)
    fname2 ='_'+y1+m1+d1+'_'+h1+m2+s2
    return fname2

college = "Nitte"
result = mcw.website_creation(college,"TeacherWebsite.txt")
print(s3)
output_zipfile = 'WebsiteCreation_'+college+time1()
shutil.make_archive(output_zipfile, 'zip' , college)
print(output_zipfile+'.zip '+s4)
time.sleep(2)
shutil.rmtree(college)
print(s1)
print(s2)
