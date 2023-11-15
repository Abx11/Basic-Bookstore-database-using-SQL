import sqlite3
try:
   db = sqlite3.connect('python_programming.db')

   cursor = db.cursor()
   cursor.execute('DROP TABLE IF EXISTS python_programming')
   db.commit()

   cursor.execute(''' 
                  CREATE TABLE IF NOT EXISTS python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
                  ''')

   db.commit()

   id1 = 55
   name1 = 'Carl Davis'
   grade1 = 61
   id2 = 66
   name2 = 'Dennis Fredrickson'
   grade2 = 88
   id3 = 77
   name3 = 'Jane Richards'
   grade3 = 78
   id4 = 12
   name4 = 'Peyton Sawyer'
   grade4 = 45
   id5 = 2
   name5 = 'Lucas Brooke'
   grade5 = 99
   student_grades = [(id1, name1, grade1), 
                     (id2, name2, grade2),
                     (id3, name3, grade3),
                     (id4, name4, grade4), 
                     (id5, name5, grade5)
                     ]


   cursor.executemany(''' 
                     INSERT INTO python_programming(id, name, grade)
                        VALUES(?, ?, ?)
                     ''', student_grades)

   # print
   db.commit()

   cursor.execute('''SELECT * FROM python_programming''')
   data = cursor.fetchall()

   for row in data:
      print(row)


   cursor.execute(''' 
                  SELECT * FROM python_programming
                  WHERE grade BETWEEN 60 AND 80
                  ''')

   selected_data = cursor.fetchall()

   print(f'\nStudents with grades between 60 and 80:')
   for row in selected_data:
      print(row)
      
      
   cursor.execute('''
                  UPDATE python_programming
                  SET grade = 65
                  WHERE id = 55
                  ''')



   cursor.execute('''SELECT * FROM python_programming''')
   print(f"\nOne update has been made to the table:\n Carl Davis' grade has been change to 65")
   data = cursor.fetchall()

   for row in data:
      print(row)

      
      
      
   cursor.execute(''' 
                  DELETE FROM python_programming
                  WHERE id = 66
                  ''')


   cursor.execute('''SELECT * FROM python_programming''')
   print(f"\nStudent 'Dennis Fredrickson' data  has been deleted from the table")
   data = cursor.fetchall()

   for row in data:
      print(row)

   cursor.execute('''
                  UPDATE python_programming
                  SET grade = 80
                  WHERE id > 55 
                  ''')

   cursor.execute('''SELECT * FROM python_programming''')
   print(f"\nStudents with id greater than 55 grade has been changed to 80:")
   data = cursor.fetchall()

   for row in data:
      print(row)
   
except sqlite3.Error as e:
   print('An error occurred:', e)

# id = cursor.lastrowid
# print('Last row id: %d' % id)
