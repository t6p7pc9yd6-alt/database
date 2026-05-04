import sqlite3
import csv
from tkinter.constants import INSERT
connection = sqlite3.connect("nepeshkom.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("""DROP TABLE IF EXISTS users""")
cursor.execute("DROP TABLE IF EXISTS samokat")
cursor.execute("DROP TABLE IF EXISTS rent")


cursor.execute("""CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age NOT NULL
)
""")
cursor.execute("""CREATE TABLE samokat(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
type TEXT NOT NULl,
price INTEGER NOT NULL,
time_rent_price TEXT NOT NULL,
full_price TEXT NOT NULL,
)
""")
cursor.execute(""" CREATE TABLE rent(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
samokat_id INTEGER NOT NULL,
borrowing_date TEXT NOT NULL,
return_date TEXT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (samokat_id) REFERENCES samokat(id)
)
""")
print("Введите свое имя")
usersname = input()
print("Введите свой возраст")
usersage = int(input())
cursor.execute(""" 
INSERT INTO users (name, age)
VALUES (?, ?)
""", (usersname, usersage))
print("Введите название самоката")
tape_name = input()
print("Введите тип самоката")
tape_type = input()
print("Введите цену аренды")
tape_time_rent_price = input()
print("Введите полную стоимость")
tape_full_price = input()
cursor.execute("""
INSERT INTO samokat (name, type , time_rent_price, full_price)
VALUES (?,?,?,?)
""",(tape_name, tape_type, tape_time_rent_price ,tape_full_price))

cursor.execute("""
INSERT INTO users (name, age)
VALUES ("Саша", 14)
""")
cursor.execute("""
INSERT INTO samokat (name, type, time_rent_price , full_price)
VALUES ("Kugoo Kirin M2 Pro", "электрический", "1000 р/с", "40000") 
""")
cursor.execute("""
INSERT INTO users (name, age)
VALUES ("Рома", 22)
""")
cursor.execute("""
INSERT INTO users (name, age)
VALUES ("Кирилл", 19)
""")
cursor.execute("""
INSERT INTO users (name, age)
VALUES ("Игнат", 47)
""")
users_array = [
    ("Маша", 32), ("Паша", 13), ("Миша", 22), ("Серафим", 25), ("Павел", 14), ("Егор", 16), ("Емеля", 23),
    ("Петя", 17), ("Педя", 45), ("Максим", 17), ("Платон", 11), ("Руслан", 24), ("Георгий", 18), ("Сергей", 17),
    ("Виталик", 15), ("Григорий", 19), ("Ахмед", 32), ("Оксана", 48), ("Амир", 50), ("гавгавгав",21), ("Рафаэль", 25),
    ("Артур", 18), ("Гоша", 35), ("Людмила", 33), ("Кира", 33), ("Михаил", 29), ("Иманбек", 27), ("Николай", 20),
    ("Алексей", 17), ("Баран", 14),
]
cursor.executemany("""
INSERT INTO users (name, age)
VALUES (?,?)
""", users_array)
samokat_array =[
("Kugoo Kirin M2 Pro", "электрический", "1000 р/д", "40000"),
    ("Kugoo Kirin M3 Pro", "электрический", "10000 р/д", "110000"),
    ("Ninebot KickScooter Max G30P", "электрический", "1500 р/д", "45000"),
    ("Kugoo C1 Pro+", "электрический", "1000 р/д", "45000"),
    ("Xiaomi Mijia M365 Electric Scooter Pro", "электрический", "1000 р/д", "42000"),
    ("Xiaomi Mi Electric Scooter 1S ", "электрический", "1000 р/д", "35000"),
    ("TRIBE Karo", "электрический", "1000 р/д", "32000"),
    ("Acer ES Series 3 Max AES203 ", "электрический", "1500 р/д", "45000"),
    ("Tordin Hermes Pro с сиденьем", "электрический", "2000 р/д", "50000"),
    ("Tordin Hermes Pro без сиденья", "электрический", "1500 р/д", "43000"),
    ("DIGMA HF8.5-4 ", "электрический", "750 р/д", "23000"),
    ("Halten Tony v.1", "электрический", "1000 р/д", "34000"),
    ("HIPER Slim VX900", "электрический", "1000 р/д", "27500"),
    ("Zaxboard ES-8i V2 Aqua", "электрический", "1000 р/д", "33000"),
    ("Ultron T103", "электрический", "3000 р/д", "Леонид 70000"),
    ("Xiaomi Electric Scooter 4 Lite EU", "электрический", "1000 р/д", "35000"),
    ("Kugoo Kirin M2+ с сиденьем", "электрический", "1500 р/д", "40000"),
    ("Kugoo Kirin M2+ без сиденья", "электрический", "1000 р/д", "35000"),
    ("Segway-Ninebot KickScooter E2 Plus", "электрический", "1000 р/д", "32000"),
    ("Accesstyle Typhoon 30S", "электрический", "1500 р/д", "45000"),
    ("HIPER Voyager MX4", "электрический", "1000 р/д", "33000"),
    ("Xiaomi Electric Scooter 3 Lite", "электрический", "1000 р/д", "30000"),
    ("Kugoo Kirin First", "электрический", "500 р/д", "20000"),
    ("MIDWAY MINI", "электрический", "750 р/д", "25000")
]
cursor.executemany("""
INSERT INTO samokat (name, type, time_rent_price, full_price)
VALUES(?,?,?,?)
""", samokat_array)
rent_array = [
(1, 1, "2024-01-10", "2024-01-20"),
    (2, 2, "2024-01-12", "2024-01-22"),
    (3, 3, "2024-01-15", "2024-01-25"),
    (4, 4, "2024-01-18", "2024-01-28"),
    (5, 5, "2024-01-20", "2024-01-30"),
    (6, 6, "2024-01-22", "2024-02-01"),
    (7, 7, "2024-01-25", "2024-02-04"),
    (8, 8, "2024-01-28", "2024-02-07"),
    (9, 9, "2024-01-30", "2024-02-09"),
    (10, 10, "2024-01-31", "2024-02-10"),
    (11, 11, "2024-02-03", "2024-02-13"),
    (12, 12, "2024-02-05", "2024-02-15"),
    (13, 13, "2024-02-07", "2024-02-17"),
    (14, 14, "2024-02-10", "2024-02-20"),
    (15, 15, "2024-03-15", "2024-03-25"),
    (16, 16, "2024-03-18", "2024-03-28"),
    (17, 17, "2024-03-25", "2024-04-04"),
    (18, 18, "2024-03-31", "2024-04-15"),
    (19, 19, "2024-03-31", "2024-04-15"),
    (20, 20, "2024-04-12", "2024-04-14"),
    (21, 21, "2024-05-03", "2024-06-01"),
    (22, 22, "2024-05-17", "2024-05-24"),
    (23, 23, "2024-05-31", "2024-06-03"),
    (24, 24, "2024-06-09", "2024-06-11"),
    (25, 25, "2024-06-22", "2024-06-30"),
    (26, 26, "2024-06-26", "2024-07-01"),
    (27, 27, "2024-07-02", "2024-07-11"),
    (28, 28, "2024-07-05", "2024-07-15"),
    (29, 29, "2024-07-16", "2024-08-03"),
    (30, 30, "2024-07-29", "2024-08-07")
]
cursor.executemany("""
INSERT INTO rent (user_id, samokat_id, borrowing_date, return_date)
VALUES(?,?,?,?)
""", rent_array)
connection.commit()
connection.close()
