"""
INTRODUCTION ABOUT PROJECT
'AUTOMATIC FILES ACCUMULATOR'

This project is Made By PRAVEEN SAHU.

This project basically arranges the all different types/extensions files into the different folders provided in the program mentioned
like folder for music,videos,pdfs,document etc.

It reduces the time to create folder when you want to accumulate 1000 to 10000 or more files which are present in your desktop and 
other files if you have in your computer than you can store it in the other folder provided or else you can leave it as it was before.. 


NOTE:- Just make sure to read the instruction at the time of program running because if you won't read and just do any process then 
the files can be moved to any other folder or it can be erased so please read it carefully.
"""

import os, time


def createIfNotExists(folder):

    global FolderList
    if not os.path.exists(f"{cwd}/{folder}"):
        os.mkdir(f"{cwd}/{folder}")   
        FolderList.append(folder)
    else:
        print("\nFolder Already Exist and files will be moved to this folder.\n")


def move(folderName, filesName):
    global filesMoved
   
    for file in filesName:
        
        os.replace(f"{cwd}/{file}", f"{cwd}/{folderName}/{file}")
        filesMoved += 1


count = 0


def details():
    global count, onlyFiles, onlyFolder
    if count == 0:

        if len(onlyFiles) == 1:
            print("File         :   ", len(onlyFiles))
        else:
            print("Files        :   ", len(onlyFiles))

        if onlyFolder == 1:
            print("\nFolder       :   ", onlyFolder)
        else:
            print("\nFolders      :   ", onlyFolder)
        count += 1


def loading():
    print("Loading", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)


print(
    """
____________________________________________________________________________________________________
                                    
                                    Automatic Files Accumulator                                
____________________________________________________________________________________________________
                                   
"""
)

print(
    "This Program accumulates all different files in different folder based on their types."
)
print(
    """
                                    ******** NOTE ********

----------------------------------------------------------------------------------------------------
Carefully look at the below mentioned Current Working Directory(CWD) first as changes will be made 
there only then do further process otherwise files/folders would be miss placed...

If CWD is not showing current folder then add folder to workspace or run program from terminal..
By writing python <Your fileName.py>
----------------------------------------------------------------------------------------------------
"""
)
# time.sleep(3.5)
menu = """

Choose from the below options: 

You can create different folders for below mentioned types:
Documents
Images
Music
Videos
PDFS
MS Office(Applications) 
Programming Languages
Others:- Files other than above mentioned types.
"""
time.sleep(1)
cwd=input("Enter working directory where you want to make folder and move the files example <C:\\New Folder>: ")
files = os.listdir(cwd)
filesMoved = 0
print(os.getcwd())
# cwd = os.getcwd()  # Current Working Directory
onlyFiles = [file for file in files if os.path.isfile(f"{cwd}/{file}")]
onlyFolder = len(files) - len(onlyFiles)


ImagesExt = [
    ".jpg",
    ".jpeg",
    ".jfif",
    ".pjpeg",
    ".pjp",
    ".png",
    ".svg",
    ".webp",
    ".gif",
    ".apng",
]
Images = [file for file in files if os.path.splitext(file)[1].lower() in ImagesExt]

DocumentsExt = [".html", ".htm", ".odt", ".ods", ".txt"]
documents = [
    file for file in files if os.path.splitext(file)[1].lower() in DocumentsExt
]

MSExt = [
    ".doc",
    ".docx",
    ".pptx",
    ".ppt",
    ".xls",
    ".xlsx",
    ".xla",
    ".xll_",
    ".xla5",
    ".xla8",
    ".xlt",
]
msapps = [file for file in files if os.path.splitext(file)[1].lower() in MSExt]

PdfsExt = [".pdf"]
pdfs = [file for file in files if os.path.splitext(file)[1].lower() in PdfsExt]

MusicsExt = [".m4a", ".mp3", ".wav", ".flac", ".m3u8", ".wma", ".aac"]
musics = [file for file in files if os.path.splitext(file)[1].lower() in MusicsExt]

VideosExt = [
    ".mp4",
    ".mov",
    ".wmv",
    ".flv",
    ".mkv",
    ".avi",
    ".webm",
    ".f4v",
    ".swf",
    "html5",
    "avchd",
]
videos = [file for file in files if os.path.splitext(file)[1].lower() in VideosExt]

PythonsExt = [".py", ".python"]
pythons = [file for file in files if os.path.splitext(file)[1].lower() in PythonsExt]

JavasExt = [".ins", ".jar", ".java", ".jnl", ".class"]
javas = [file for file in files if os.path.splitext(file)[1].lower() in JavasExt]

CsExt = [
    ".c",
]
cs = [file for file in files if os.path.splitext(file)[1].lower() in CsExt]

CPlusExt = [
    ".cpp",
    ".cc",
]
cplus = [file for file in files if os.path.splitext(file)[1].lower() in CPlusExt]

# print(f"Now total files and folders are : {len(files)}\n")
if len(onlyFiles) == 1 or len(onlyFiles) == 0:
    file = "file"
else:
    file = "files"
if onlyFolder == 1 or onlyFolder == 0:
    folder = "folder"
else:
    folder = "folders"
print(
    f"\nTotal {len(files)} ({len(onlyFiles)} {file} and {onlyFolder} {folder}) in Current Working Directory: -------- {cwd} --------"
)
loading()
print("\n----------------------\n")
print("Documents    :   ", len(documents))
print("Images       :   ", len(Images))
print("Musics       :   ", len(musics))
print("Videos       :   ", len(videos))
print("PDFS         :   ", len(pdfs))
print("MS Office    :   ", len(msapps))
print("C Files      :   ", len(cplus))
print("Python Files :   ", len(pythons))
print("C++ Files    :   ", len(cs))
print("Java Files   :   ", len(javas))
others = len(onlyFiles) - (
    len(documents)
    + len(Images)
    + len(musics)
    + len(videos)
    + len(pdfs)
    + len(msapps)
    + len(cs)
    + len(pythons)
    + len(cplus)
    + len(javas)
)
print("Others       :   ", others)
print("\n----------------------")

details()


def checkFolderName(folder, name):

    checkpoint = "True"
    while checkpoint == "True":
        try:
            folder = input(f"For {name}: ")

            a = 0
            for element in range(0, len(folder)):

                if (
                    folder == " "
                    or folder == "\n"
                    or folder[element] == "\\"
                    or folder[element] == "/"
                    or folder[element] == "*"
                    or folder[element] == ":"
                    or folder[element] == "?"
                    or folder[element] == '"'
                    or folder[element] == "<"
                    or folder[element] == ">"
                    or folder[element] == "|"
                    or (folder[-1:-3:-1]=="..")
                ):
                    print(
                        "ERROR!!!!!\nYou entered wrong folder name\nPlease re-enter the folder name!!!\n"
                    )
                    a = +1
                    break

            if a == 0:
                createIfNotExists(folder)
                checkpoint = "False"
                # print("Checkpoint false folder created")
                return folder
        except Exception as e:
            print(
                "Please Give Some name to the folder!!! instead of just pressing Enter!!!\n"
            )


# \ / : * ? " < > |
print(menu)
FolderList = []
loading()
print("\n\nEnter folders name one by one according to your choice\n")
print(
    """                         NOTE:- 
                      -----------
1) Folder name should not contain (# \ / : * ? " < > |) characters 
      
2) Write .(dot) If you don't want to create folder or want files to replace/move
   in the same location as it is 
                    
3) Write ..(double dot) If you don't want to create folder or want files to move in the
   parent folder of CWD
"""
)
DocumentName = (
    ImagesName
) = (
    MusicName
) = (
    PdfsName
) = (
    CsName
) = PythonsName = CPlusName = MSName = JavasName = VideosName = OthersName = None
DocumentName = checkFolderName(DocumentName, "Document")
ImagesName = checkFolderName(ImagesName, "Images")
MusicName = checkFolderName(MusicName, "Musics")
VideosName = checkFolderName(VideosName, "Videos")
PdfsName = checkFolderName(PdfsName, "PDFs")
MSName = checkFolderName(MSName, "MS Applications")
CsName = checkFolderName(CsName, "C Files")
PythonsName = checkFolderName(PythonsName, "Python Files")
CPlusName = checkFolderName(CPlusName, "C++ Files")
JavasName = checkFolderName(JavasName, "Java Files")

check = "True"
while check == "True":
    option = input(
        """\nWould you like to store all other files in different folder??? 
        
Press 1. For Yes
Press 2. For No  """
    )
    if option == "1":

        OthersName = checkFolderName(OthersName, "Other Files")
        others = []
        for file in files:
            extensions = os.path.splitext(file)[1].lower()

            if (
                (extensions not in MusicsExt)
                and (extensions not in VideosExt)
                and (extensions not in DocumentsExt)
                and (extensions not in MSExt)
                and (extensions not in PdfsExt)
                and (extensions not in ImagesExt)
                and (extensions not in CsExt)
                and (extensions not in PythonsExt)
                and (extensions not in CPlusExt)
                and (extensions not in JavasExt)
                and os.path.isfile(f"{cwd}/{file}")
            ):
                others.append(file)
            check = "False"

    elif option == "2":
        check = "False"

    else:
        print("\nInvalid entry!!! Please enter from the above given option only..")
try:
    move(DocumentName, documents)
    move(ImagesName, Images)
    move(MusicName, musics)
    move(VideosName, videos)
    move(PdfsName, pdfs)
    move(MSName, msapps)
    move(CsName, cs)
    move(PythonsName, pythons)
    move(CPlusName, cplus)
    move(JavasName, javas)
    if option == "1":
        move(OthersName, others)
    time.sleep(1)
except Exception as e:
    print("File Can't be moved due to incorrect folder name!!!!\n\n", e)


AfterFiles = os.listdir(cwd)
AfterOnlyFiles = [AfterFile for AfterFile in AfterFiles if os.path.isfile(f"{cwd}/{AfterFile}")]
newFilesCreated = len(onlyFiles) - len(AfterOnlyFiles)
if newFilesCreated == 1:
    newFilesCreatedString = "file"
    print(
        f"\n{newFilesCreated} {newFilesCreatedString} has been moved to different folder"
    )
elif newFilesCreated == 0:
    print(f"\nNothing has been moved to any folder")

elif (newFilesCreated != 1 and onlyFolder != 1) or (
    newFilesCreated != 0 and onlyFolder != 0
):
    newFilesCreatedString = "files"
    print(
        f"\n{newFilesCreated} {newFilesCreatedString} have been moved to different folders"
    )


if len(FolderList) != 0:
    print("\nThese are the new folders created :")

Number = 0
for index, items in enumerate(FolderList):
    if FolderList[index] != ".":
        Number += 1
        print("*", items)
if Number == 1:
    print(f"Total {Number} folder has been created.")

elif Number == 0:
    pass
else:
    print(f"Total {Number} folders have been created.")


if Number == 0:
    print("\nNo folder has been created.")

if len(AfterOnlyFiles) == 1:
    file = "file"
elif len(AfterOnlyFiles) != 1 and len(AfterFiles) - len(AfterOnlyFiles) == 1:
    file = "files"
    folder = "folder"
else:
    file = "files"
    folder = "folders"


if len(AfterFiles) == 1 or len(AfterFiles) == 0:
    item = "item"
else:
    item = "items"
print(
    f"\nNow total {len(AfterFiles)} {item} ({len(AfterOnlyFiles)} {file} and {len(AfterFiles)-len(AfterOnlyFiles)} {folder}) are there in {cwd}"
)

time.sleep(4)
