import json
import random

try:
    with open('data.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)
except Exception as error:
    print(f"Произошла ошибка: {error}")
print(tasks)

def new_task(a, b, c):
    id = random.randint(1000, 9999)
    tasks.append(dict(ID = id, name = a, description = b, status = c))
            
def task_completed(ID):
    for task in tasks:
        if task["ID"] == ID:
            task["status"] = 1
            
def delete_task(ID):
    for task in tasks:
        if task["ID"] == ID:
            tasks.remove(task)
            
def read_tasks():
    print(tasks)
            
new_task("обед", "погреть еду в микроволновке", 0)
read_tasks()

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(tasks, file, ensure_ascii=False, indent=4)



