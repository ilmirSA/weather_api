import random
import sqlite3

# пример данных
user_data = [
    (1, 'Oleg', random.randint(5000, 15000)),
    (2, 'Vladimir', random.randint(5000, 15000)),
    (3, 'Aleksey', random.randint(5000, 15000)),
    (4, 'Michael', random.randint(5000, 15000)),
    (5, 'Olga', random.randint(5000, 15000)),
]


class User:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        '''Создаем таблицу users'''
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, balance INTEGER)''')
        self.conn.commit()

    def add_test_user(self):
        '''Добавляем тестовых юзеров'''
        self.cursor.executemany("REPLACE INTO users (id,username, balance) VALUES (?, ?,?) ", user_data)
        self.conn.commit()

    def update_user_balance(self, user_id, new_balance):
        '''Обновляем баланс на новое значение'''
        self.cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
        self.conn.commit()

    def get_user_balance(self, user_id):
        """Получаем баланс юзера"""
        self.cursor.execute(f"SELECT balance FROM users WHERE id={user_id}")
        balance = self.cursor.fetchall()
        return balance[0][0]

    def delete_user(self, username):
        '''Удаляем юзера'''
        self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.conn.commit()
