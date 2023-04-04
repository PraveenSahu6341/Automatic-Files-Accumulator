"""
INTRODUCTION ABOUT PROJECT
'AUTOMATIC FILES ACCUMULATOR'

This project is Made By PRAVEEN SAHU.

This project is based Graphical User interface,basically it arranges all different types/extensions files into the different folders provided in the program mentioned
like folder for music,videos,pdfs,document etc.

It reduces the time to create folder when you want to accumulate 1000 to 10000 or more files which are present in your desktop and 
other files if you have in your computer than you can store it in the other folder provided or else you can leave it as it was before.. 


NOTE:- Just make sure to read the instruction at the time of program running because if you won't read and just do any process then 
the files can be moved to any other folder or it can be erased so please read it carefully.
"""

from tkinter import * ;import os;from tkinter.messagebox import  askyesno, showerror, showinfo
from tkinter.font import Font
import time


def declarations(name, index):
    scindex = StringVar()
    scindex.set("")
    listSc.append(scindex)
    lbl = Label(f1, text=f"{name}: ", font= "sans-serif 12 bold")
    entryName = Entry(f1,textvar=listSc[index],justify="center",bg="yellow",fg="red",font=("Times", 12, "bold"),highlightthickness=2,)
    list_entry.append(entryName)
    Folder_Btn = Button(f1,text="Create Folder",font="Arial 10 bold",bg="#55B4B0",fg="white",activeforeground="white",activebackground="#BFD641",command=lambda: createfolder(index, name, Folder_Btn, a))
    Folder_Btn.grid(row=index + 2, column=3, padx=10)
    entryName.config(highlightbackground="red", highlightcolor="red")
    lbl.grid(sticky="w", row=index + 2, column=0, padx=10, pady=5)
    entryName.grid(row=index + 2, column=1, padx=10)
    if name[-1]=='s':
        name=name[:-1]
    list_names.append(name)
    
    
def hideCreateFolder(index,Folder_Btn,path,Path):
    Folder_Btn.destroy()
    list_entry[index].config(state=DISABLED)
    moveBtn = Button(f1,text="   Move   ",font="Arial 10 bold",bg="#55B4B0",fg="white",activeforeground="white",activebackground="#BFD641",command=lambda: folderExt(index,path,Path,moveBtn))
    moveBtn.grid(row=index + 2, column=3)     
    f1.config(padx=10)
    
def createIfNotExists(folder,index,Folder_Btn):
    global folder_name,parent_dir
    Path=parent_dir+"\\"
    path = os.path.join(Path, folder)
    if os.path.isdir(path):
        answer=askyesno("Folder Already Exists","Want to continue with this folder???")
        if answer==0:
             listSc[index].set("")
        else:
            hideCreateFolder(index,Folder_Btn,path,Path)        
    elif not os.path.exists(folder):
        os.mkdir(path)
        hideCreateFolder(index,Folder_Btn,path,Path)
    elif os.path.exists(folder):
        if folder.lower()=="Images".lower() or folder.lower()=="Documents".lower() or folder.lower()=="Audios".lower() or folder.lower()=="Videos".lower() or folder.lower()=="PDFs".lower() or folder.lower()=="Others".lower():
            os.mkdir(path)
            hideCreateFolder(index,Folder_Btn,path,Path)
            
def folderExt(index,path,Path,moveBtn):
    files = os.listdir(Path)
    ImagesExt = [".jpg",".jpeg",".jfif",".pjpeg",".pjp",".png",".svg",".webp",".gif",".apng"]
    DocumentsExt = [".odt", ".ods", ".txt"]
    VideosExt = [".mp4",".mov",".wmv",".flv",".mkv",".avi",".webm",".f4v",".swf","html5","avchd"]
    MusicsExt = [".m4a", ".mp3", ".wav", ".flac", ".m3u8", ".wma", ".aac"]
    MSExt = [".doc",".docx",".pptx",".ppt",".xls",".xlsx",".xla",".xll_",".xla5",".xla8",".xlt",".rtf"]
    PdfsExt = [".pdf"]
    CsExt = [".c",]
    PythonsExt = [".py", ".python"]
    CPlusExt = [".cpp", ".cc",]
    JavasExt = [".ins", ".jar", ".java", ".jnl", ".class"]
    match index:
        case 0:
            Images = [file for file in files if os.path.splitext(file)[1].lower() in ImagesExt]
            move(Images,index,path,moveBtn,Path)
        case 1:
            documents = [file for file in files if os.path.splitext(file)[1].lower() in DocumentsExt]
            move(documents,index,path,moveBtn,Path)
        case 2:
            videos = [file for file in files if os.path.splitext(file)[1].lower() in VideosExt]
            move(videos,index,path,moveBtn,Path)
        case 3:
            musics = [file for file in files if os.path.splitext(file)[1].lower() in MusicsExt]
            move(musics,index,path,moveBtn,Path)
        case 4:
            msapps = [file for file in files if os.path.splitext(file)[1].lower() in MSExt]
            move(msapps,index,path,moveBtn,Path)
        case 5:
            pdfs = [file for file in files if os.path.splitext(file)[1].lower() in PdfsExt]
            move(pdfs,index,path,moveBtn,Path)
        case 6:
            cs = [file for file in files if os.path.splitext(file)[1].lower() in CsExt]
            move(cs,index,path,moveBtn,Path)
        case 7:
            pythons = [file for file in files if os.path.splitext(file)[1].lower() in PythonsExt]
            move(pythons,index,path,moveBtn,Path)
        case 8:
            cplus = [file for file in files if os.path.splitext(file)[1].lower() in CPlusExt]
            move(cplus,index,path,moveBtn,Path)
        case 9:
            javas = [file for file in files if os.path.splitext(file)[1].lower() in JavasExt]
            move(javas,index,path,moveBtn,Path)
        case 10:
            other = []
            for file in files:
                extensions = os.path.splitext(file)[1].lower()
                if ( (extensions not in MusicsExt) and (extensions not in VideosExt) and (extensions not in DocumentsExt) and (extensions not in MSExt) and (extensions not in PdfsExt) and (extensions not in ImagesExt) and (extensions not in CsExt) and (extensions not in PythonsExt) and (extensions not in CPlusExt) and (extensions not in JavasExt) and os.path.isfile(f"{parent_dir}/{file}")
                ):
                    other.append(file)
            move(other,index,path,moveBtn,Path)

def restore(filesName,index,path,moveBtn,Path,restoreBtn):
    try:
        for file in filesName:
            os.replace( f"{path}/{file}",f"{parent_dir}/{file}")
        if(len(filesName)==1 and not ((index==4) or (index==6) or (index==7) or (index==8) or (index==9) or (index==10))) :
            showinfo("Restored File",f"{len(filesName)} {list_names[index]} restored.")
        elif (not ((index==4) or (index==6) or (index==7) or (index==8) or (index==9) or (index==10))):
            showinfo("Moved Files",f"{len(filesName)} {list_names[index]}s restored. ")
        elif len(filesName)==1:
            showinfo("Restored Files",f"{len(filesName)} {list_names[index]} file restored. ")
        else:
            showinfo("Restored Files",f"{len(filesName)} {list_names[index]} files restored. ")
            
        
    except Exception as e:
        showerror("FileNotFoundError",f"{e}")
    
    moveBtn = Button(f1,text="   Move   ",font="Arial 10 bold",bg="#55B4B0",fg="white",activeforeground="white",activebackground="#BFD641",command=lambda: folderExt(index,path,Path,moveBtn))
    moveBtn.grid(row=index + 2, column=3)
    restoreBtn.destroy()
    
def move(filesName,index,path,moveBtn,Path):
    global passing_arguments,list_entry
    if(filesName==[] and not ((index==4) or (index==6) or (index==7) or (index==8) or (index==9) or (index==10))) :
        showinfo(f"No {passing_arguments[index]}",f"No {list_names[index]} in {Path}")
    elif(filesName==[]) :
        showinfo(f"No {passing_arguments[index]} files",f"No {list_names[index]} files in {Path}")
    else:   
        for file in filesName:
            os.replace(f"{parent_dir}/{file}", f"{path}/{file}")
      
        if(len(filesName)==1 and not ((index==4) or (index==6) or (index==7) or (index==8) or (index==9) or (index==10))) :
            showinfo("Moved File",f"{len(filesName)} {list_names[index]} moved to {list_entry[index].get()} folder. ")
        elif (not ((index==4) or (index==6) or (index==7) or (index==8) or (index==9) or (index==10))):
            showinfo("Moved Files",f"{len(filesName)} {list_names[index]}s moved to {list_entry[index].get()} folder. ")
        elif len(filesName)==1:
            showinfo("Moved File",f"{len(filesName)} {list_names[index]} file moved to {list_entry[index].get()} folder. ")
        else:
            showinfo("Moved Files",f"{len(filesName)} {list_names[index]} files moved to {list_entry[index].get()} folder. ")
        restoreBtn= Button(f1,text=" Restore ",font="Arial 10 bold",bg="#55B4B0",fg="white",activeforeground="white",activebackground="#BFD641",command=lambda:restore(filesName,index,path,moveBtn,Path,restoreBtn))
        restoreBtn.grid(row=index + 2, column=3)
        moveBtn.destroy()
        
def help():
    showinfo("Making folders under the given directory!!!","For making the folder and moving the files you have to give the path first\n\nCOPY THE PATH FROM THE ADDRESS BAR AND PASTE IT UNDER THE ENTRY BOX OF THE SHOWN FIELD OR YOU CAN MANUALLY TYPE \n\n According to the path given it will create the folder under that directory and if the path is incorrect then the folder won't be created.")
    

def createfolder(index, name, Folder_Btn, a):
    try:
        folder_name = list_entry[index].get().strip()
        folder = folder_name
        if list_entry[index].index("end") == 0:
            showerror(
                """FolderName Error !!""", """FOLDER NAME SHOULD NOT BE EMPTY ! !""")
        else:
            for element in range(0, len(folder)):
                if (folder == " " or folder == "\n" or folder[element] == "\\" or folder[element] == "/" or folder[element] == "*" or folder[element] == ":" or folder[element] == "?" or folder[element] == '"' or folder[element] == "<" or folder[element] == ">" or folder[element] == "|" or (folder[-1:-3:-1] == "..")):
                    folder_name = ""
                    listSc[index].set("")
                    showerror("""FolderName Error""","""Enter Valid Folder Name\nDon't Include < > .. " ' \ / ? * : |""")
                    list_entry[index].update()
                    a = 1
                    break
            if a == 0:
                createIfNotExists(folder,index,Folder_Btn)
    except Exception as e:
        showerror("Error","Please Enter Correctly Error")
      
def readInfo():
    showinfo(
        """Important Information !!""",
        """UNDER ENTRY BOX - Enter the name of the folder to be made.
             \nPRESS CREATE FOLDER - To create folder in the current(path) directory.
             \nPRESS MOVE BUTTON   - To move the files in the folder.
             \n\nIf you don't want to move files then enter (. single dot) in the folder name""")

def about():
    showinfo(
        """ABOUT - Automatic Files Accumulator""",
        """\t       | Automatic Files Accumulator | 
            \n\nThis is Files Accumulator, what it does is that if you have various files of different types\extensions it searches for same types of files and it groups all the same extension files in single folder provided by the user.
              \n\nThis basically ease your work by grouping the files and it saves your time as it doesn't take much time to do this.
              \nAnd in case if you want to get back your moved files in the exisiting location and you can also restore them.
              \n\n\nMade By := PRAVEEN SAHU""")

def path_dir():
    check="True"
    while check=="True":
        global parent_dir
        parent_dir = pathEntry.get().strip()
        if parent_dir=="" or parent_dir=="." or parent_dir=="/" or (parent_dir[-1:-3:-1] == "..") or parent_dir=="\\" or os.path.isdir(parent_dir)==False:
            pathEntry.delete(0,END)
            showerror("""PathName Error""","""Path Not Found\nEnter Valid Path Name\n""")
            break
        else: 
            check="False"
            starter.destroy()
            infoBtn.destroy()
            submitBtn.destroy()
           
            global BtnT,f0,f1
            f1 = Frame(root, highlightthickness=5, padx=5,pady=20)
            Button(f1,text="Read this first",command=readInfo,font=my_font,bg="red",fg="white",activeforeground="red",activebackground="yellow",highlightbackground="cyan",padx=5,pady=4).grid(row=0, column=0, columnspan=4)
            f0 = Frame(f1, bg="red").grid(pady=10)
            global passing_arguments
            for i in range(0,11):
                declarations(passing_arguments[i],i)
            f1.config(highlightbackground="orange", highlightcolor="orange")
            f1.pack(pady="30 0")   
            
root = Tk()
root.title("Files Accumulator GUI")
root.geometry("480x630")
root.config(bg="yellow")
a=0
list_entry,list_names,listSc = [],[],[]
passing_arguments=["Images","Documents","Videos","Audios","MS Office","PDFs","C","Python","C++","Java","Other"]
my_font = Font(family="Arial",size=10,weight="bold", slant = 'roman', underline = 1,overstrike=0,)

titleBtn = Button(root,text="Automatic Files Accumulator",font=("sans-serif",20, "bold"),bg="black",fg="white",command=about).pack(fill=X)
starter = Frame(root, highlightthickness=5, height=30,width=40,highlightbackground="orange",padx=5)
Button(starter,text="ABOUT THIS",command=about,font=my_font,bg="red",fg="white",activeforeground="red",activebackground="yellow",highlightbackground="cyan",padx=5,pady=4).grid(row=0, column=0, columnspan=4,pady=20)
path_label=Label(starter,text="ENTER PATH WHERE YOU WANT TO MOVE \nFILES TO FOLDER: ",font= "sans-serif 12 bold").grid(row=1,column=1)
pathEntry=Entry(starter, width=55,font="sans-serif 10 bold",bg="yellow",highlightthickness=2,highlightcolor="red",highlightbackground="red")
pathEntry.grid(row=2,column=0,columnspan=4,pady=10,padx=10)
infoBtn=Button(root,text="HELP ?",font="sans-serif 10 bold",bg="black",fg="white",activeforeground="black",activebackground="white",command=lambda:help())
submitBtn=Button(starter,text="SUBMIT",font="sans-serif 10 bold",bg="#55B4B0",fg="white",activeforeground="white",activebackground="#BFD641",command=lambda:path_dir())
submitBtn.grid(row=3,column=0,columnspan=2,pady=10)
starter.pack(pady=135)
infoBtn.pack()

root.mainloop()
time.sleep(2)
