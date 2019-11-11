import csv
filename = "test.csv"
a = ["asd", "dfgh"]
with open(filename, "a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(a)