import csv

from expense_manager import add_transaction

def import_from_csv(filepath):
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            add_transaction(row['date'], row['description'], float(row['amount']), int(row['category_id']))
            
         