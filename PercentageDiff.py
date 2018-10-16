import csv

csv_rows = []
with open('GlobalLandTemperaturesByCountry2003-13_F.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    title = reader.fieldnames
    for row in reader:
        csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
old_value = 0
new_value = 0
final_list = []
final_list.append(reader.fieldnames)
temp_list = []
keys = []
#print(csv_rows)
for row in csv_rows:
    if row['Year'] == '2003':
        old_value = float(row['AverTempYear'])
    elif row['Year'] == '2013':
        new_value = float(row['AverTempYear'])
        percent = (new_value - old_value) / old_value
        row['AverTempYear'] = percent
        keys = row.keys()
        #print(keys)
        for key in keys:
            temp_list.append(row[key])
        #print(temp_list)
        final_list.append(temp_list)
        temp_list = []
        old_value = 0
        new_value = 0

print(final_list)

with open("TemperatureDiff.csv", "w") as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerows(final_list)