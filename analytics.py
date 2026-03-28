import sqlite3

from database import initialise_database

def total_spent():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(transaction_amount) FROM transactions;")
        total = cursor.fetchall()
        return total

def spent_per_category():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT category_id, SUM(transaction_amount) FROM transactions GROUP BY category_id;")
        category_total = cursor.fetchall()
        return category_total

def transactions_by_date(date):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE transaction_date = ?", (date,))
        category_total = cursor.fetchall()
        return category_total



