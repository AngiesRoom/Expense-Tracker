import sqlite3

from database import initialise_database

def add_budget(spending_limit, budget_period, category_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO budgets(spending_limit, budget_period, category_id) VALUES (?, ?, ?)", (spending_limit, budget_period, category_id,))
        conn.commit()


def get_all_budgets():
    with sqlite3.connect('database.db') as conn:
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM budgets")
      results = cursor.fetchall()
      return results
     

if __name__ == '__main__':
   

   answer = get_all_budgets()
   print(answer)