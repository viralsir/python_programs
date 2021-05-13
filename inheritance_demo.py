'''
inheritance : is the proccess by which object of one class can
 access or get the properties of object of another class.

 A

 A a1=A();
 B(A)

 B b1=B();
 category of inheritance :
 1)Single Inheritance : one object can access the properties of only one
 object at a time .
        A   parent class/ base class / super class
        |
        B   child class / derive class / sub class
 2) Multilevel Inheritance : continous chain of single inheritance .
        A
        |
        B
        |
        C
 3) Hyrarchical Inheritance : more than object can access the
 properties of same object
                   A
            |               |
            B               C

 4) multiple inheritance : one object can access or
 get the properties of more than one object at a time.
             A              B
                    |
                    C
 5) Hybrid Inheritance : combination of more than
 one inheritance
                      Personal_info
                       |
          Student           Teacher     employee
            |                |          |
                    School

    logical inheritance : --
    simple application : notedown

  RTO Registrations

  Hospital appointment



'''
class Personal_info:
    id=0
    name=""
    addres=""
    phno=""

    def setPersonal_info(self):
        self.id=int(input("Enter Id :"))
        self.name=input("Enter Name :")
        self.addres=input("Enter address:")
        self.phno=input("Enter phno:")

    def getPersonal_info(self):
        print("id:",self.id)
        print("Name:",self.name)
        print("address:",self.addres)
        print("Phno:",self.phno)

class Student(Personal_info):
      maths=0

      def setStudent(self):
          self.setPersonal_info()
          self.maths=int(input("Enter Maths :"))

      def getStudent(self):
          self.getPersonal_info()
          print("Maths :",self.maths)

class Teacher(Personal_info):
    subject=""
    salary=""

    def setTeacher(self):
        self.subject=input("Enter Subject :")
        self.salary=int(input("Enter Salary :"))

    def getTeacher(self):
        print("subject:",self.subject)
        print("salary :",self.salary)


class School(Student,Teacher):
    board=""
    address=""

    def setSchool(self):
        self.board=input("Enter board:")
        self.address=input("Enter Address:")

    def getSchool(self):
        print("board :",self.board)
        print("address:",self.address)



s=School()
s.setStudent()
s.setTeacher()
s.setSchool()

# s1=Student()
# s1.setPersonal_info()
# t1=Teacher()
# t1.setPersonal_info()
#
#
# s1.getPersonal_info()
# t1.getPersonal_info()

# s1=School()
# #s1.setPersonal_info()
# s1.setSchool()
# s1.setStudent()
#
# print("output ")
# s1.getSchool()
# s1.getStudent()
















