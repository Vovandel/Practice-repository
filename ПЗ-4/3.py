import json
import random

#Функция для обновления содержимого файла
def update_file():
    try:
        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(students, file)
    except Exception as error:
        print(f'Возникла ошибка: {error}')

try:
    with open('students.json', 'r', encoding='utf-8') as file:
        students = json.load(file)
except Exception as error:
    print(f"Возникла ошибка: {error}")

while True:
    print('''>>>>>>>>>>>>>>>Введите команду<<<<<<<<<<<<<<
          1 - добавить студента
          2 - вывод списка студентов
          3 - поиск по имени
          4 - расчёт среднего балла для студента
          5 - выйти
          ''')
    choice = int(input())
    
    if choice == 1:
        id = random.randint(100,999)
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        if age <= 16:
            print('Студент слишком маленький :(')
            continue
        group = input("Введите группу: ")
        marks = input("Введите оценки (2-5) через пробел:").split()
        for x in marks:
            if not(2<=int(x)<=5):
                print('Неверная оценка, введите число от 2 до 5')
                continue
        students.append(dict(ID = id, Name = name, Age = age, Group = group, Marks = marks))
        update_file()
        
    elif choice == 2:
        for x in students:
            print(x)
            continue
        
    elif choice == 3:
        search_name = input("Введите имя студента: ")
        for x in students:
            if x.get('Name') == search_name:
                print("Студент найден")
                print(x)
                continue
            
    elif choice == 4:
        search_id = int(input("Введите ID студента: "))
        for x in students:
            if x.get('ID') == search_id:
                marks = x.get('Marks')
                sr = 0
                for x in marks:
                    sr += int(x)
                sr /= len(marks)
                print('Средний балл: ' + str(sr))
                continue
            
    elif choice == 5:
        break