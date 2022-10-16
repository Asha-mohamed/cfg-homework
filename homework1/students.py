class Student:
    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = subjects


class CFGStudent(Student):
    def __init__(self, name, age, id, subjects, specialisation):
        super(CFGStudent, self).__init__(name, age, id, subjects)
        self.specialisation = specialisation

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

    def view_subjects(self):
        for subject in self.subjects:
            print(subject)

    def average_grade(self):
        total_grade = 0
        for subject in self.subjects:
            total_grade += subject["grade"]
        return total_grade / len(self.subjects)


Asha = CFGStudent("Asha", 25, 342, [], "software")
Asha.add_subject({"name": "python", "grade": 99})
Asha.add_subject({"name": "SQL", "grade": 100})
Asha.add_subject({"name": "OOP", "grade": 75})
print("Subjects so far ")
Asha.view_subjects()
Asha.remove_subject({"name": "OOP", "grade": 75})
print("Subjects after removal ")
Asha.view_subjects()
print("Average grade")
print(Asha.average_grade())
