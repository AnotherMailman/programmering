class Car:
    def __init__(self, brand : str, color : str, speed : int):
        self.brand = brand
        self.color = color
        self.speed = speed

    def __str__(self):
        return f"a {self.color} {self.brand}"

    def change_color(self, new_color : str):
        self.color = new_color 
        

class Student:
    def __init__(self, f_name : str, l_name : str, year : int, grades : list):
        self.f_name = f_name
        self.l_name = l_name
        self.year = year
        self.grades = grades
    
    def add_grade(self, new_grade : int):
        self.grades.append(new_grade)

    def avarage_grade(self):
        print(round(sum(self.grades) / len(self.grades), 1))
    
    def student_info(self):
        print(f"{self.f_name} {self.l_name}")

class Classroom:
    def __init__(self, name : str, class_list : list[Student]):
        pass

volvo1 = Car("Volvo", "Black", 2000000000000000000)
print(volvo1.color)
volvo1.change_color("White")

student1 = Student("Harald", "Stenhård", 2021, [4, 3, 4, 2, 1])
student2 = Student("Härlord", "Steinhard", 2022, [1, 1, 1, 5, 1])
student3 = Student("Hanlock", "Stanhåld", 2023, [1, 2, 1, 2, 1])

student3.add_grade(2)
student3.avarage_grade()
student3.student_info()