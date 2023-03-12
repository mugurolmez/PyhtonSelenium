students=["mehmet","ali","hasan","hakan"]
numbers=[2,3,7]


def studentManyAdd():
    student1=input("1. Öğrenciyi ekleyiniz: ")
    student2=input("2. Öğrenciyi ekleyiniz: ")
    student3=input("3. Öğrenciyi ekleyiniz: ")
    students.extend([student1,student2,student3])
    print("Öğrenciler Eklendi")
    ListOfStudents()

def ListOfStudents():
    print("güncel Öğrenci Listesi")
    for student in students:
        print(str(students.index(student))+" "+student)

def studentAdd():
    student=input("Yeni Öğrencinin isim ve Soyisimini Yazınız: ")
    students.append(student)
    print("öğrenci eklendi "+str(students.index(student))+" "+student)
    ListOfStudents()


def studentDelete():
    student=input("Silinmesini İstediğiniz isim ve Soyisimini Yazınız: ")
    students.remove(student)

def getStudentNumber():
    studentname=input("Numarasını Oğrenmek İstediğiniz Öğrencinin İsimini Soyismini Giriniz: ")
    print("öğrencinin Numarası: " +str(students.index(studentname)))


def studentManyDelete():
        ListOfStudents()
         
        number1=input("silinmesini istediğiniz 1. öğrencinin numarasını giriniz: ")
        number2=input("silinmesini istediğiniz 2. öğrencinin numarasını giriniz: ")
        number3=input("silinmesini istediğiniz 3. öğrencinin numarasını giriniz: ")

        numbers=[number1,number2,number3]
        studentnames=[]

        for i in range(0,len(numbers)):
              studentnames.append(students[int(numbers[i])])  
             
             
    
        print(studentnames)
        j=0
        while j<len(numbers):
                students.remove(studentnames[j])
                j+=1

        ListOfStudents()

                
studentManyDelete()


