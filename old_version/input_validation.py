import csv
import os


def amount_of_statements():
    is_amount_of_statements_valid = False
    while not is_amount_of_statements_valid:
        try:
            amount_of_statements = int(input("How many statements do have? "))
            if amount_of_statements <= 0:
                print("Invalid Input")
            else:
                is_amount_of_statements_valid = True
        except ValueError:
            print("Please enter an integer")


def validate_files():
    valid_fieldname = ['Date', 'Description', 'Amount']
    current_folder = os.path.dirname(__file__)
    csv_files = []
    valid_csv_files = []

    for files in os.listdir(current_folder):
        if files.lower().endswith(".csv"):
            csv_files.append(files)

    for i in range(len(csv_files)):
        with open(csv_files[i]) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            if valid_fieldname == csv_reader.fieldnames:
                valid_csv_files.append(csv_files[i])
    return valid_csv_files


def export_row(date, description, amount):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'Output')
    output_file = os.path.join(output_dir, 'TFL Output.csv')
    with open(output_file, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, description, amount])

def wipe_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'Output')
    output_file = os.path.join(output_dir, 'TFL Output.csv')
    with open(output_file, mode='w', newline='') as csvfile:
        pass
