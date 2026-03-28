import sqlite3

from database import initialise_database

def check_budgets():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT category_name, SUM(transaction_amount), spending_limit FROM transactions JOIN  budgets ON transactions.category_id = budgets.category_id JOIN " \
        "categories ON categories.category_id=budgets.category_id GROUP BY category_id ")
        results = cursor.fetchall()
        alerts = []
        for row in results:
            if row[1] > row[2]:
                message = "Over budget"
                alerts.append(message)
            elif row[1] > 0.8* row[2]:
                message = "You are almost overbudget"
                alerts.append(message)
            else:
                message = "You are on track"
                alerts.append(message)
        return alerts
            
