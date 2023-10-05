file = open("students.txt", "w")
for i in range(2):
    name = input("Введите фамилию студента: ")
    while any(char.isdigit() for char in name):
        print("Фамилия студента не должна содержать цифры.")
        name = input("Введите фамилию студента: ")
    grades = []
    for j in range(5):
        while True:
            try:
                grade = int(input("Введите оценку по предмету: "))
                break
            except ValueError:
                print("Оценка должна быть числом.")

        grades.append(grade)

    average_grade = sum(grades) / len(grades)
    file.write(name + " " + str(average_grade) + "\n")
file.close()

file = open("students.txt", "r")
for line in file:
    name, average_grade = line.split()
    average_grade = float(average_grade)

    if average_grade > 8:
        print(f"Фамилия студента: {name}, Средний балл: {average_grade}")
file.close()