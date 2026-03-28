import sqlite3


def initialise_database():

 with sqlite3.connect('database.db') as conn:

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
                   category_id integer primary key autoincrement,
                   category_name text
                   )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions(
                   transaction_id integer primary key,
                   transaction_date text,
                   transaction_description text,
                   transaction_amount real,
                   category_id integer,
                   FOREIGN KEY(category_id) REFERENCES categories(category_id)
                    )

    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS budgets(
                   budget_id integer primary key,
                   spending_limit real,
                   budget_period text,
                   category_id integer,
                   FOREIGN KEY(category_id) REFERENCES categories(category_id)
                   
                   )
    ''')

    

if __name__ == '__main__':
  initialise_database()
  print('Database ready')