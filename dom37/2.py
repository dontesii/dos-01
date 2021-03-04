class Students():
    def __init__(self, name, lastname, klass, acad):
        self.name = name
        self.lastname = lastname
        self.kalss = klass
        self.acad = acad

    def show_students(self):
        discription = (" Name is : " + self.name +'\n' + " Lastname is: "  + self.lastname +'\n' + " Klass is: " + str(self.kalss) +'\n' + " Academ is: " + str(self.acad)+'\n').title()
        print(discription)

students1 = Students("Dmitriy","Chueshkov", 11, 7)
students2 = Students("Nikola","Regik", 19, 7)

students1.show_students()
students2.show_students()