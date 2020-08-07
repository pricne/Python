"""
Schedulers & File Handling

Read all files in a specific folder and store in JSON Format with Date Created, Date Modified, File Name, File Extension & File Size.
Create a Scheduler that scans the folder every 1 minute and adds any new files to the JSON File.

File Handling link: https://drive.google.com/file/d/14KAGHgKIewL3zBj1kBUnIajbVlcB7kda/view?usp=sharing

"""
import os, time, json
Location = input("Enter Folder Location : ")
Folder_Name = input("Enter Folder Name : ")
#Location = "C:/Users/OMOLP059/Desktop/2.Scheduler&File_Handling"
#Folder_Name = "2.Scheduler&File_Handling"
i = 0
fileName = []
fileExtension = []
fileSize = []
fileCreatedTime = []
fileModifiedTime = []
onlyfiles = []

os.chdir(Location)
No_of_files = os.listdir(Location)
mydict = {}



def print_data():
    for i in range(len(No_of_files)-1):
        print("File_Name : ",fileName[i])
        print("File_Extension : ",fileExtension[i])
        print("File_Size : ",fileSize[i])
        print("Date_Created : ",fileCreatedTime[i])
        print("Date_Modified : ",fileModifiedTime[i])

def Get_data(Position):
    fileName.clear()
    fileExtension.clear()
    fileSize.clear()
    fileCreatedTime.clear()
    fileModifiedTime.clear()
    onlyfiles = [f for f in No_of_files if os.path.isfile(os.path.join(Position, f))]
    
    for files in onlyfiles:
        Name,Extension = os.path.splitext(files)            #split filename and extention
        Size = os.stat(files).st_size                       #get size of file
        Created_time = time.ctime(os.path.getctime(files))  #get created time of file
        modified_time = time.ctime(os.path.getmtime(files)) #get modified time of file
        fileName.append(Name)                               #append name in List
        fileExtension.append(Extension)                     #append Extention in List
        fileSize.append((str(Size>>10)+"KB"))               #convet size in KB and append in List
        fileCreatedTime.append(Created_time)
        fileModifiedTime.append(modified_time)
        
def dict_format():
    mydict[Folder_Name] = []
    for i in range(len(No_of_files)-1):
        mydict[Folder_Name].append({
            'File Name': fileName[i],
            'File Extension': fileExtension[i],
            'File Size': fileSize[i],
            'Date Created': fileCreatedTime[i],
            'Date Modified': fileModifiedTime[i],
        })

try:
    Get_data(Location)
    #print_data()
    dict_format()

    app_json = json.dumps(mydict)
    print(app_json)
    while True:
        if len(No_of_files) != len(os.listdir(Location)):         # check if file is updated
            print("New File Added")
            No_of_files.clear()
            No_of_files = os.listdir(Location)
            print(No_of_files)
            Get_data(Location)
            dict_format()

            app_json = json.dumps(mydict)
            print(app_json)
        else:
            pass
            #print("No File Added")

        time.sleep(60)#time in Seconds i.e 60seconds
        
except KeyboardInterrupt:
    print("Quitting the program.")
except:
    print("Unexpected error")
    raise

    
