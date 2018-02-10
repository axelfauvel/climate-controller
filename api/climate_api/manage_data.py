import sqlite3

class ManageDatabase:
    def __init__(self):
        self.db = sqlite3.connect('status.db')
        self.cursor = self.db.cursor()

    def init_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS status(power TEXT, ac_mode TEXT, temperature TEXT, fan TEXT)
        ''')
        self.db.commit()

    def get_status(self):
        self.cursor.execute('''SELECT power, ac_mode, temperature, fan from status''')
        return self.cursor.fetchone()

    def set_status(self, power, temperature, ac_mode, fan):
        self.cursor.execute(''' DELETE FROM TABLE status''')
        self.cursor.execute(''' INSERT INTO status(power, ac_mode, temperature, fan) VALUES(?,?,?,?)''',
                            (power, ac_mode, temperature, fan))
        self.db.commit()