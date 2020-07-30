f=open("note.dat",'a')
numberofstudent=int(input("numberofstudent"))
for i in range(numberofstudent):
    nameofstudent=input("studentname")
    studentrollno=int(input("studentroll"))
    studenttotal=int(input("studenttotal"))
    studentpass="pass"
    studentfail="fail"
    f.write(str(nameofstudent))
    f.write("\t")
    f.write(str(studentrollno))
    f.write("\t")
    f.write(str(studenttotal))
    f.write("\t")
    if(studenttotal>=300):
      print("pass")
      f.write(studentpass)
    else:
      print("fail")
      f.write(studentfail) 
    f.write("\n")
f.close()


