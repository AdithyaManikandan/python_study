numberofstudent=int(input("num of student:"))
print(numberofstudent)
for i in range(numberofstudent):
    studentsnames=input("name of the student:")
    studentsrollnumber=int(input("roll no of the students:"))
    studentstotal=int(input("students total:"))
    if(studentstotal>=350):
        print("pass")
    else:
        print("fail")