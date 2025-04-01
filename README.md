print("FILE CONTENT IS AS FOLLOWS : ")
file1=open("sample.txt","r")
reading= file1.readline()
reading1= file1.readline()
print("FIRST LINE : ",reading)
print("SECOND LINE : ",reading1)
file1.close()
try:
    open("sample.txt")
except FileNotFoundError:
    print("YOUR FILE ","sample.txt"," CANNOT BE FOUND")
    print("FILE CONTENT COULD NOT BE FOUND")
