l_name=["Ritu" , "Khushi","Abhay","Abhishek"]
l_marks=[60,60,50,50]
l_increment=[5,-7,5,-5]
s="-"
m=1
def name_add(name):
    l_name.append(name)
def marks_add(marks):
    l_marks.append(marks)
def increment_add(increment):
    l_increment.append(increment)
def _1():
    l_add=[]
    a=input("Name of Student: ")
    name_add(a)
    l_add.append(a)
    b=int(input("initial marks of student: "))
    marks_add(b)
    l_add.append(b)
    c=int(input("increment marks of students: "))
    increment_add(c)
    l_add.append(c)
    print("data you have added:",l_add)
    print()
def _2():
    a=input("name of student whose record you want to update: ")
    m=l_name.index(a)
    print("Data you want to update :\n1)Marks \n2)Increment")
    i=int(input("S.no. of object you want to update: "))
    if i==1:
        l=int(input("Marks now:"))
        l_marks[m]=l
    elif i==2:
        l=int(input("Increment now:"))
        l_increment[m]=l
    print("Data of student now:")
    print(l_name[m],l_marks[m],l_increment[m],end=" ,")
    print()
def _3():
    m=input("Name of student u want to delete data: ")
    d=l_name.index(m)
    l_name.pop(d)
    l_marks.pop(d)
    l_increment.pop(d)
    print()
def _5():
    for i in range(0,len(l_name)):
        print(s*48)
        print("|",l_name[i]," "*(15-len(l_name[i])),"|",l_marks[i]," "*(15-len(str(l_marks[i]))),"|",l_increment[i]," "*(5-len(str(l_increment[i]))),"|")
    print(s*48)
    print()
def _6():
       l_final=[]
       for i in range(0,len(l_marks)):
           l_final.append(str(l_marks[i]+l_increment[i])+l_name[i])
       for i in range(0,len(l_marks)):
           l_final.sort(reverse=True)
           print(i+1,"  -  ",l_final[i][2:],"  -  ",l_final[i][:2])
       print()
while m>0:
    print("1)add data of one more student.\n2)Update data \n3)delete data \n4)Acess data \n5)Compare final Rank of Students\n6)Exit")
    y=int(input("Task no. u want to perform: "))
    if y==1:
        _1()
    elif y==2:
        _2()
    elif y==3:
        _3()
    elif y==4:
        _5()
    elif y==5:
        _6()
    elif y==6:
        m-=1

           
           
       

