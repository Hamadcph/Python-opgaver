import csv


file_path = 'C:\\Users\\hamad\\OneDrive\\Dokumenter\\Datamatiker\\4.semester\\Python\\SemesterPlan\\Exercises\\OPGAVER\\uge2\\.ipynb_checkpoints\\test.csv'

with open(file_path, newline='') as f:
    reader = csv.reader(f)
    myList = list(reader)

print(myList)
