import json
import datetime
import random

def add_note(): #ввод и сохранение заметки
    with open("save.json", "r+") as file:
        notes = json.load(file)

        note = {}
        note["id"] = random.randint(100,1000)
        note["title"] = input("Введите заголовок: ")
        note["text"] = input("Введите текст: ")
        note["date_creation"] = datetime.datetime.today().strftime('%d-%m-%Y')
        note["time_creation"] = datetime.datetime.now().strftime("%H:%M:%S")

        flag = True
        while flag:
            if note["id"] in notes: note["id"] = random.randint(100,1000)
            else: flag = False
        notes[note["id"]] = note

        file.seek(0) 
        file.truncate() #удаление старого
        json.dump(notes, file, indent=3) #запись нового
        print("Запись сохранена.")

def get_notes(): #вывод всех заметок
    with open("save.json", "r") as file:
        notes = json.load(file)
        if notes == {}:
            print("Файл пуст.")
        else:
            i = 0
            for key in notes:
                print(notes[key])

def get_note(): #вывод одной заметки по id
    open_id = str(input("Введите id открываемой записки: "))
    with open("save.json", "r") as file:
        if open_id in notes:
            notes = json.load(file)
            print(notes[open_id])
        else:
            print("id не существует")

def edit_note(): #редактирование по id
    edit_id = str(input("Введите id редактируемой записки: "))
    with open("save.json", "r+") as file:
        if edit_id in notes:
            notes = json.load(file)
            note = notes[edit_id]
            note["title"] = input("Введите новый заголовок: ")
            note["text"] = input("Введите новый текст: ")

            file.seek(0) 
            file.truncate() #удаление старого
            json.dump(notes, file, indent=3) #запись нового
            print("Запись изменена.")
        else:
            print("id не существует")

def del_note(): #удаление по id
    del_id = str(input("Введите id удаляемой записки: "))
    with open("save.json", "r+") as file:
        notes = json.load(file)

        if del_id in notes:
            del notes[del_id]

            file.seek(0) 
            file.truncate() 
            json.dump(notes, file, indent=3) 

            print("Запись удалена.")
        else:
            print("id не существует")

def get_notes_date():    
    start_date_input = input("Введите начальную дату (дд-мм-гггг): ")
    end_date_input = input("Введите конечную дату (дд-мм-гггг): ")
    
    with open("save.json", "r") as file:
        notes = json.load(file)
        start_date = datetime.datetime.strptime(start_date_input, "%d-%m-%Y")
        end_date = datetime.datetime.strptime(end_date_input, "%d-%m-%Y")
        print_notes =[]

        for note in notes.values():
            note_date = datetime.datetime.strptime(note["date_creation"], "%d-%m-%Y")
            if start_date <= note_date <= end_date:
                print_notes.append(note)
    print(print_notes)
        

def main():
    flag =  True
    while flag:
        command = input("Введите команду: ")
        if command == "add":
            add_note()
        elif command == "help":
            text = """
add--добавление заметок;
Ng--вывод заметки по id;
del--удаление заметки по id;
edit--редактирование заметки по id;
Nlist--вывод списка заметок;
Ndate--вывод списка заметок c промежутке конкретной даты
"""
            print(text)
        elif command == "Ng":
            get_note()
        elif command == "del":
            del_note()
        elif command == "edit":
            edit_note()
        elif command == "Nlist":
            get_notes()
        elif command == "exit":
            flag = False
            print("Завершение работы.")
        elif command == "Ndate":
            get_notes_date()
        else:
            print("Неизвестная команда, введите help для вывода списка команд")

try:
    with open("save.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    with open("save.json", "w") as file:
        json.dump({}, file)

main()