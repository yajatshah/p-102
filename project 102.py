import os
import shutil

source="C:/Users/yajat/OneDrive/Desktop"
destination="C:/Users/yajat/OneDrive/Desktop/abc"

list_of_files=os.listdir(source)
print(list_of_files)
for i in list_of_files:
    name,ext=os.path.splitext(i)
    if ext=="":
     continue
    if ext in ['.txt', '.doc', '.docx','.pdf']:
     path1 = source + '/' + i
     path2 = destination + '/' + "docx_files"
     path3 = destination + '/' + "docx_files" + '/' + i

    if os.path.exists(path2):
     print("moving")
     shutil.move(path1,path3)
    else:
     os.makedirs(path2)
     print("moving")
     shutil.move(path1,path3)

 