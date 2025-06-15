import sqlite3
from dotenv import load_dotenv
load_dotenv()

##Connect to the database(SQLite)
connection = sqlite3.connect("student.db")

##Create a cursor object insertion, creation and retrieval
cursor = connection.cursor()

##Create a table
table_info='''
Create table if not exists STUDENT(NAME VARCHAR(25) NOT NULL, CLASS VARCHAR(25) NOT NULL, ROLL_NO INT PRIMARY KEY NOT NULL, SECTION VARCHAR(25) NOT NULL, MARKS INT NOT NULL);
'''
cursor.execute(table_info)

##Insert data into the table
cursor.execute('''Insert into STUDENT values 
  ('Satyam',        'GenerativeAI',   50,  'A',  100), 
  ('Ananya',        'MachineLearning',123, 'A',  92),
  ('Rohan',         'DataScience',    312, 'B',  85),
  ('Priya',         'CyberSecurity',  589, 'A',  78),
  ('Vikram',        'CloudComputing', 274, 'C',  88),
  ('Meera',         'DevOps',         831, 'B',  91),
  ('Arjun',         'AI Ethics',      406, 'A',  73),
  ('Nisha',         'Robotics',       957, 'C',  82),
  ('Karan',         'IoT',            618, 'B',  89),
  ('Sneha',         'Blockchain',     742, 'A',  95),
  ('Dev',           'QuantumComputing',365,'C',  67),
  ('Rhea',          'NLP',            294, 'B',  90),
  ('Tanvi',         'ComputerVision', 583, 'A',  84),
  ('Kabir',         'BigData',        476, 'C',  79),
  ('Lina',          'UX/UI',          139, 'B',  87),
  ('Yash',          'AR/VR',          908, 'A',  93)''')

##Display the data in the table
print("Data in the table:")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

##Close the connection
connection.commit()
connection.close()