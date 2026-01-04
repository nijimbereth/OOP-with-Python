#Using properties to avoid that fellow programmers change an element in the code

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} lives in {self.house}"

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name missing")
        self._name = name

    @property
    def house(self):
        return self._house
        
    @house.setter
    def house(self, house):
        if house not in ["Oldenburg", "Edewecht", "Bremen", "Hannover"]:
            raise ValueError("Invalid Input")
        self._house = house

def get_student():
    name = input("What's your name? ")
    house = input("Where do you live? ")
    return Student(name, house)

def main():
    student = get_student()
    Student.house = "Berlin"
    print(student)

if __name__=="__main__":
    main()