try:
    filename = input("Введите имя файла: ")
    with open(filename, mode = 'a', encoding='utf-8') as file:
        file.write(input("Введите строку которую надо добавить в файл: "))
    with open(filename, mode = 'r', encoding='utf-8') as file:
        print("Содержимое файла после добавления: " + file.read())
except Exception as error:
    print(f"Произошла ошибка: {error}")