import csv
import input_validation as validate

validate.wipe_file()
csv_files = validate.validate_files()
validate.export_row('Date', 'Description', 'Amount')
for file in csv_files:

    print(f'{file} Statement')

    with open(file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)

        headers = {header: [] for header in reader.fieldnames}

        for row in reader:
            for header, value in row.items():
                headers[header].append(value)

    valid_index = []
    date_charges = {}

    for i, date in enumerate(headers['Description']):
        if headers['Description'][i] == 'TFL TRAVEL CHARGE       TFL.GOV.UK/CP':
            valid_index.append(i)

    for i in valid_index:
        date = headers['Date'][i]
        cost = float(headers['Amount'][i])

        if date in date_charges:
            date_charges[date] += cost
        else:
            date_charges[date] = cost

    total_cost = 0
    for date, total in date_charges.items():
        print(f'{date} TFL TRAVEL CHARGE       TFL.GOV.UK/CP {round(total, 2)}')
        validate.export_row(date, 'TFL TRAVEL CHARGE       TFL.GOV.UK/CP', round(total, 2))
        total_cost += total

    total_cost = round(total_cost, 2)
    print(f'Total TFL Charges: {total_cost}')
    print()
    print(headers)
    print(date_charges)