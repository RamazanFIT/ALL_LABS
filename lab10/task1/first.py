import psycopg2
import csv
connect = psycopg2.connect( 
    host = "localhost",
    database = "testb",
    user = "postgres",
    password = "Akkenzhe70"
)
cur = connect.cursor()
go_to = "SOME"
while go_to != "STOP":
    go_to = input()
    
    if go_to == "1":
        for i in range(10):
            print()
        print("Enter a name: ")
        name = input()
        print("Enter a surname: ")
        surname = input()
        print("Enter a phone number: ")
        telephone = input()
        cur.execute(f"INSERT INTO some_data (name,surname, tel) VALUES ('{name}', '{surname}' , '{telephone}')")
        connect.commit()
        print("Successfully entered into database.")
    elif go_to == "2":
        for i in range(10):
            print()
        print("Смена имени пользователя: ")
        print("Введите пожалуйста ваш номер телефона: ")
        tel_change = input()
        print("Спасибо")
        print("Введите имя на которую хотите сменить: ")
        name = input()
        print("Введите фамилию на которую хотите сменить: ")
        surname = input()
        cur.execute(f"UPDATE some_data SET name = '{name}', surname = '{surname}' WHERE tel = '{tel_change}'")
        print("Успешно изменен.")
        connect.commit()
    elif go_to == "3":
        for i in range(10):
            print()
        print("Смена номера: ")
        print("Введите имя: ")
        name = input()
        print("Введите фамилию: ")
        surname = input()
        print("Введите номер на которую хотите изменить: ")
        tel_change = input()
        print("Происходит изменение")
        cur.execute(f"UPDATE some_data SET tel = '{tel_change}' WHERE name = '{name}' AND surname = '{surname}'")
        print("Успешно")
        connect.commit()
    elif go_to == "4":
        for i in range(10):
            print()
        print("Удаление пользователя: ")
        print("Пожалуйста введите номер телефона который хотите удалить: ")
        tel = input()
        cur.execute(f"DELETE FROM some_data WHERE tel = '{tel}'")
        print("Success")
        connect.commit()
    elif go_to == "5":
        for i in range(10):
            print()
        file = open("data.csv", "r")
        file = csv.reader(file)
        next(file)
        for value in file:
            cur.execute(f"INSERT INTO some_data (name, surname, tel) VALUES ('{value[0]}', '{value[1]}', '{value[2]}')")
        connect.commit()
    elif go_to == "6":
        for i in range(10):
            print()
        print("Sorting by name of the table: ")
        cur.execute("SELECT * FROM some_data ORDER BY name")
        data = cur.fetchall()
        for row in data:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    elif go_to == "7":
        for i in range(10):
            print()
        print("Sorting by surname of the table: ")
        cur.execute("SELECT * FROM some_data ORDER BY surname")
        data = cur.fetchall()
        for row in data:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    elif go_to == "8":
        for i in range(10):
            print()
        print("Sorting by telephone number of the table: ")
        cur.execute("SELECT * FROM some_data ORDER BY tel")
        data = cur.fetchall()
        for row in data:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    
    elif go_to == "0":
        for i in range(10):
            print()
        print("Stopped")
        go_to = "STOP"
        cur.close()
        connect.close()




