import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, 
    book_titles TEXT, 
    authors_names TEXT,
    names_of_publishing_houses TEXT,
    the_year_of_publishing INTEGER,
    number_of_pages INTEGER,
    number_of_illustrations INTEGER,
    price INTEGER,
    name_of_the_library_branches_where_the_book_is_located TEXT,
    number_of_students_who_received_the_book INTEGER) """
    cursor.execute(query)
    db.commit()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS record(id INTEGER PRIMARY KEY,
    book_id iNTEGER,
    branch_id INTEGER,
    amount INTEGER) """
    cursor.execute(query)
    db.commit()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS branch(id INTEGER PRIMARY KEY,
    name_branch TEXT,
    data_id INTEGER) """
    cursor.execute(query)
    db.commit()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS faculty(id INTEGER PRIMARY KEY,
    name_faculty TEXT) """
    cursor.execute(query)
    db.commit()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY,
    branch_id INTEGER,
    faculty_id INTEGER)  """
    cursor.execute(query)
    db.commit()

insert_data1 = [
    (1, 'Бесы', 'Достоевский', 'Графа', 1896, 749, 1, 930, 'Центральный', 2),
    (2, 'Тошнота', 'Сартр', 'АртБук', 1910, 540, 2, 340, 'Восточный', 5),
    (3, 'Капитал', 'Маркс', 'Годность', 1859, 1500, 10, 159, 'Северный', 15),
    (4, '1984', 'Оруэл', 'Донпечать', 1943, 543, 4, 380, 'Центральный', 8),
    (5, 'ОНО', 'КИНГ', 'Графа', 1987, 1040, 2, 1080, 'Северный', 30),
    (6, 'Мы', 'Замятин', 'Донпечать', 1873, 410, 3, 250, 'Центральный', 14),
]
# with sqlite3.connect('database.db') as db:
#   cursor = db.cursor()
#   query = """ INSERT INTO book (id, book_titles, authors_names, names_of_publishing_houses, the_year_of_publishing,
#   number_of_pages, number_of_illustrations, price, name_of_the_library_branches_where_the_book_is_located,
#   number_of_students_who_received_the_book)
#   VALUES(?,?,?,?,?,?,?,?,?,?) """
#   cursor.executemany(query, insert_data1)
#   db.commit()

insert_data2 = [(1, 1, 1, 4),
                (2, 2, 2, 8),
                (3, 3, 3, 20),
                (4, 4, 1, 24),
                (5, 5, 3, 40),
                (6, 6, 1, 30), ]

# with sqlite3.connect('database.db') as db:
#    cursor = db.cursor()
#    query = """ INSERT INTO record (id, book_id, branch_id, amount ) VALUES(?,?,?,?) """
#    cursor.executemany(query, insert_data2)
#    db.commit()

insert_data3 = [(1, 1, 'Центральный'),
                (2, 2, 'Восточный'),
                (3, 3, 'Северный'),
                ]

# with sqlite3.connect('database.db') as db:
#   cursor = db.cursor()
#   query = """ INSERT INTO branch (id, data_id, name_branch) VALUES(?,?,?) """
#   cursor.executemany(query, insert_data3)
#   db.commit()

insert_data4 = [(1, 'Философский'),
                (2, 'Экономический'),
                (3, 'Художественный'),
                ]

# with sqlite3.connect('database.db') as db:
#    cursor = db.cursor()
#    query = """ INSERT INTO faculty (id, name_faculty) VALUES(?,?) """
#    cursor.executemany(query, insert_data4)
#    db.commit()

insert_data5 = [(1, 1, 1),
                (2, 2, 2),
                (3, 3, 3),
                ]

# with sqlite3.connect('database.db') as db:
#   cursor = db.cursor()
#   query = """ INSERT INTO data (id, branch_id, faculty_id) VALUES(?,?,?) """
#   cursor.executemany(query, insert_data5)
#   db.commit()
print(
    'Выберите действие: 1 - Для филиала посчитать количество экземпляров указанной книги, находящихся в нём \n'
    '2 - Для указанной книги посчитать количество факультетов на котором она используется \n'
    '3 - Возможность добавления и изменения информации о книгах в библиотеке \n' 
    '4 - Возможность добавления и изменения информации о филиалах '
)
a = int(input())
if a == 1:
    # ЗАДАНИЕ 1 Для указанного филиала посчитать количество экземпляров указанной книги, находящихся в нём
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        cursor.execute(""" SELECT amount FROM record JOIN book ON book_id = book.id WHERE book_titles = 'Капиталы' and branch_id = 4 """)
        sum = 0
        for res in cursor:
            sum += res[0]
            print(res)
        print('TOTAL: ', sum)
if a == 2:
    # ЗАДАНИЕ 2 Для указанной книги посчитать количество факультетов на котором она используется
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        query = """SELECT count(*) FROM faculty WHERE id IN (
     SELECT faculty_id FROM data WHERE branch_id IN (
     SELECT branch_id FROM record WHERE book_id = (
     SELECT id FROM book WHERE book_titles = 'Бесы'
      ) ) )"""

        cursor.execute(query)
        sum = 0
        for res in cursor:
            sum += res[0]
            print(res)
        print('TOTAL: ', sum)
if a == 3:
    # ЗАДАНИЕ 3 Предоставить возможность добавления и изменения информации о книгах в библиотеке
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute("UPDATE book SET book_titles = 'Капиталы' WHERE id = 3")
if a == 4:
    # Задание 4 Предоставить возможность добавления и изменения информации о филиалах
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute("UPDATE branch SET name_branch = 'Центральное' WHERE id = 1")

# Задание 5 Предусмотреть разработку триггеров предполагающих каскадные изменения в связных таблицах

# with sqlite3.connect('database.db') as db:
#    cursor = db.cursor()
#
#    cursor.execute(" CREATE TRIGGER update_user AFTER UPDATE ON book "
#                   "FOR EACH ROW "
#                   "BEGIN "
#                   "    UPDATE record SET amount = 1 WHERE id = OLD.id; "
#                   "END; " )
