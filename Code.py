a=str(input("FILE NAME : "))
try :
    file=open(a,"r")
    reading=file.readline()
    print("FIRST LINE IS : ",reading)
    reading1=file.readline()
    print("SECOND LINE IS : ",reading1)
except FileExistsError:
    print("SORRY ! The file does not exists")
except FileNotFoundError:
    print("SORRY ! But the file cannot be found")
