noOfStudents=int(input("enter a number:\t"))
#print(noOfStudents)

f=open("test.dat",'a')
for i in range(noOfStudents):
    rollno=input("rollno of the student:\t")
    name=input("name of the student:\t")
    total_mark=int(input("total mark of the student:\t"))
    f.write(rollno)
    f.write("\t")
    f.write(name)
    f.write("\t")
    f.write(str(total_mark))
    f.write("\t")
    if(total_mark>=350):
        print("pass")
        f.write("pass")
    else:
        print("fail")
        f.write("fail")
    f.write("\n")
f.close()
#123    Magil   500
#124    Solai   55