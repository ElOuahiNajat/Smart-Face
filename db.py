import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.con = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.con.cursor()

    def insert(self, nom, Performance, Poste, email, Gender, Department, image_data):
        sql = "INSERT INTO employee (nom, Performance, Poste, email, Gender, Department, IMAGE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (nom, Performance, Poste, email, Gender, Department, image_data)
        self.cur.execute(sql, values)
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT id, nom, Performance, Poste, email, Gender, Department, IMAGE FROM employee")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM employee WHERE id=%s", (id,))
        self.con.commit()

    def update(self, id, nom, Performance, Poste, email, Gender, Department, image_data):
        sql = "UPDATE employee SET nom=%s, Performance=%s, Poste=%s, email=%s, Gender=%s, Department=%s, IMAGE=%s WHERE id=%s"
        values = (nom, Performance, Poste, email, Gender, Department, image_data, id)
        self.cur.execute(sql, values)
        self.con.commit()

    def search(self, criterion, value):
        sql = f"SELECT * FROM employee WHERE {criterion}=%s"
        self.cur.execute(sql, (value,))
        rows = self.cur.fetchall()
        return rows
