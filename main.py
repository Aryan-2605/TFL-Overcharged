import csv
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