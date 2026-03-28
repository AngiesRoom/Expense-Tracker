import sqlite3

from database import initialise_database

def add_transaction(date, description, amount, category_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (transaction_date, transaction_description, transaction_amount, category_id) VALUES (?, ?, ?, ?)", (date, description, amount, category_id,))
        conn.commit()

def get_all_transactions():
    with sqlite3.connect('database.db') as conn:
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM transactions")
     results = cursor.fetchall()
     return results
     
    

if __name__ == '__main__':

   answer = get_all_transactions()
   print(answer)