'''creating a program that recieves users' input and prints the data'''
#In this situation we deal with names of students and their place of residence

def main():
    print(get_student())


def get_student():
    name = input("What's your name? ")
    house = input("Where do you live? ")
    return f"{name} lives in {house}"

if __name__=="__main__":
    main()


    