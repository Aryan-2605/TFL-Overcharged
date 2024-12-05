import csv
import pandas as pd
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

file_names = []

for i in range(amount_of_statements):
    input_file = input("Enter file name include .csv: ")




with open('activity.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)

    headers = {header: [] for header in reader.fieldnames}

    for row in reader:
        for header, value in row.items():
            headers[header].append(value)

#for header, values in headers.items():
    #print(f'{header}: {values}')

#index = headers['Date'].index('03/12/2024')
#print(index)

valid_index = []

for i, date in enumerate(headers['Description']):
    if headers['Description'][i] == 'TFL TRAVEL CHARGE       TFL.GOV.UK/CP':
        valid_index.append(i)

#print(valid_index)
cost = 0
for i in valid_index:
    cost += float(headers['Amount'][i])
    print(headers['Date'][i], headers['Description'][i], headers['Amount'][i])


cost = round(cost, 2)
print(f'Total cost: {cost}')