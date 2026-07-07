students = []

def add_students():
        name =input("Enter a student name: ")
        for student in students:
                if name == student[0]:
                        print("User alread exists")
                        return
                
        marks= int(input("Enter a students marks : "))
        new_student=[name,marks]
        students.append(new_student)
        print(students)
        
        

def delete_students():
        name  = input("Enter a name: ")
        for i in students:
                if i[0] == name:
                        students.remove(i)
                        print("deleted successfully !!")

def search_student():
        name = input("Enter a name: ")
        found = False 
        for record in students:
                if record[0] == name:
                        found = True
                        print(f"Student Found\n--------------------\nname  : {record[0]}\nMarks : {record[1]}\n--------------------")
                        break
        if not found :
                print("Student not found")

def update_marks():
        name = input("Enter a name: ") 
        found = False                   
        for record in students:
                if name == record[0]:
                        found = True
                        print(f"Current marks are:  {record[1]}")
                        new_marks= int(input("Enter a new marks: "))
                        record[1] = new_marks
                        print("Marks update successfully")
                        break
        if not found:
                print("User not found")


def display_students():
        for record in students:
                print(f"name  : {record[0]}\nMarks : {record[1]}\n--------------------")


def main():

        while True:
                print("1.add students")
                print("2.delete students")
                print("3.search student")
                print("4.update marks")
                print("5.display students")
                print("6.Exit")

                user = int(input("Enter a number: "))

                if user == 1:
                        add_students()
                
                elif user ==2:
                        delete_students()

                elif user ==3:
                        search_student()
                
                elif user ==4:
                        update_marks()

                elif user==5:
                        display_students()
                
                elif user ==6:
                        print("Exiting")
                        break

main()