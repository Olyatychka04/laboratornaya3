with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку (пустая строка для окончания ввода): ")
        if line == "":
            break
        f1.write(line + "\n")

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    even_lines = [line.strip() for index, line in enumerate(lines) if index % 2 == 1]
    f2.write("\n".join(even_lines))

with open("F2.txt", "r") as f2:
    first_line = f2.readline().strip()
    word_count = len(first_line.split())
    print("Количество слов в первой строке файла F2:", word_count)
