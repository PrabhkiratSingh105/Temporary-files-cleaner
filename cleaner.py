from os import getcwd,chdir,remove,listdir
from shutil import rmtree
from time import sleep
C=""
while(getcwd() != "C:\\"):
	for i in range(len(getcwd().split("\\"))-1):
    		C += "..\\"
chdir(C+"Windows\Temp\\")
def temp():
    files=0
    if(listdir()!=[]):
        for i in listdir():
            if(i[-4] == "."):
                try:
                    remove(i)
                    files += 1
                except:
                    pass
            else:
                try:
                    i=i.split(".")
                    i=".".join(i)
                    remove(i)
                    files+=1
                except:
                    pass
                try:
                    rmtree(i)
                    files += 1
                except:
                    try:
                        chdir(f"{i}\\")
                        temp()
                    except:
                        pass
    return files
files=temp()
chdir("..\..\\")
company = ""
array = ['Dell', 'HP', 'Lenovo', 'Acer', 'Asus', 'Toshiba', 'Samsung', 'MSI', 'Alienware', 'Gateway', 'Fujitsu', 'Panasonic', 'LG']
for i in listdir("Users\\"):
    for value in array:
        if value == i:
            company = i
chdir(f"Users\{company}\AppData\Local\Temp\\")
def Hp(file):
    files=file
    if(listdir()!=[]):
        for i in listdir():
            if(i[-4] == "."):
                try:
                    remove(i)
                    files += 1
                except:
                    pass
            else:
                try:
                    i=i.split(".")
                    i=".".join(i)
                    remove(i)
                    files+=1
                except:
                    pass
                try:
                    rmtree(i)
                    files += 1
                except:
                    try:
                        chdir(f"{i}\\")
                        Hp(files)
                    except:
                        pass
    return files
files=Hp(files)
try:
    from plyer import notification 
    notification.notify(title="Cleaner",message=f"{str(files)} temporary files got cleared",timeout=5)
except: print(f"{str(files)} temporary files got cleared")
sleep(5)