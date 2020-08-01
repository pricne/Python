#read file from folder and save in a list
#Make a seperate list for File name and Extention 
import os, time
i = 0
fileName = []
fileExtension = []
fileSize = []
fileCreatedTime = []
fileModifiedTime = []
onlyfiles = []
Location = "C:/Users/OMOLP059/Desktop/2.Scheduler&File_Handling"
os.chdir(Location)
files = os.listdir(Location)

def print_data():
    for i in range(len(files)-1):
        print("File_Name : ",fileName[i])
        print("File_Extension : ",fileExtension[i])
        print("File_Size : ",fileSize[i])
        print("Date_Created : ",fileCreatedTime[i])
        print("Date_Modified : ",fileModifiedTime[i])

def Get_data(Position):
    onlyfiles = [f for f in files if os.path.isfile(os.path.join(Position, f))]
    #print(onlyfiles)                   # print list with all files and extention
    
    for files in onlyfiles:
        Name,Extension = os.path.splitext(files)
        Size = os.stat(files).st_size
        Created_time = time.ctime(os.path.getctime(files))
        modified_time = time.ctime(os.path.getmtime(files))
        fileName.append(Name)            #append name in List
        fileExtension.append(Extension)  #append Extention in List
        fileSize.append((str(Size>>10)+"KB"))        #convet size in KB and append in List
        fileCreatedTime.append(Created_time)
        fileModifiedTime.append(modified_time)
        
         

Get_data(Location)
print_data()
'''
#print(onlyfiles)# print list with all files and extention
print(fileName)   # It print file name
print(fileExtension)   # Print File Extensions
print(fileSize)   # It print file size
print(fileCreatedTime)   # It print file size
print(fileModifiedTime)   # It print file size
'''



    
