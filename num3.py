file = open("subjects.txt", "w")
file.write("Математика: лекционных - 3, практических - 5\n")
file.write("Физика: лекционных - 2, лабораторных - 4\n")
file.write("Информатика: практических - 6, лабораторных - 3\n")
file.close()

subject_dict = {}
read_file = open("subjects.txt", "r")
lines = read_file.readlines()
read_file.close()

for line in lines:
    line = line.strip()
    subject = line.split(":")[0]
    lectures = 0
    practicals = 0
    labs = 0
    if "лекционных" in line:
        lectures = int(line.split("лекционных - ")[1].split(",")[0])
    if "практических" in line:
        practicals = int(line.split("практических - ")[1].split(",")[0])
    if "лабораторных" in line:
        labs = int(line.split("лабораторных - ")[1])
    total_lessons = lectures + practicals + labs
    subject_dict[subject] = total_lessons
print(subject_dict)