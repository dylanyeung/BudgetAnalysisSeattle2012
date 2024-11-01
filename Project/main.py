import csv

with open("city-of-seattle-2012-expenditures-dollars.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    #skip header line
    next(reader)

    #dictionary to store department name and expenses
    dictionary = {}
    for value in reader:
        #set variables for each column value in the current line
        department, bcl, program, actual, adopted, endorsed, proposed = value
        previous_value = 0

        if department == '':
            department = "N/A"
        if actual == '':
            actual_value = 0
        else:
            actual_value = int(actual)
        #if there is already an entry in the dictionary for a key, add the previous value to the new value
        if department in dictionary:
            previous_value = int(dictionary.get(department))

        dictionary[department] = previous_value + actual_value


#print department name and sum of their 2012 expenditure
for key, value in dictionary.items():
    print(key + f": ${value:,.2f}")