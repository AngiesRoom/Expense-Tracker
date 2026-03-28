import sqlite3

from database import initialise_database 

def add_category(name):
    
 with sqlite3.connect('database.db') as conn:
   cursor = conn.cursor()
   cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (name,))

   conn.commit()
    
def get_all_categories():
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    results = cursor.fetchall()
    return results
    
    
if __name__ == '__main__':
  
  answer = get_all_categories()
  print(answer)

