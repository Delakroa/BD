import sqlite3 as sl

con = sl.connect('my-test.db')

with con:
    con.execute("""
        CREATE TABLE USER(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)

sql = 'INSERT INTO USER (id, name, age) values(?,?,?)'
data = [
    (1, 'Vovan', 32),
    (2, 'Diman', 34),
    (3, 'Oleg', 37),
]

with con:
    con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM USER WHERE age <=37")
    for row in data:
        print(row)
