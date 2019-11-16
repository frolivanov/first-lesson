import csv

FILENAME = 'interesting_files.csv'

users = [
    ['tom',28],
    ['alice',23],
    ['bob',34]
]

with open(FILENAME,'w',newline='',) as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, 'a',newline='') as file:
    user = ['sam',31]
    writer = csv.writer(file)
    writer.writerow(user)