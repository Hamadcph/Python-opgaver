# 1. `def print_file_content(file)` that can print content of a csv file to the console
import csv


file_path = 'C:\\Users\\hamad\\OneDrive\\Dokumenter\\Datamatiker\\4.semester\\Python\\SemesterPlan\\Exercises\\OPGAVER\\uge2\\.ipynb_checkpoints\\test.csv'
with open(file_path) as f:
    reader = csv.reader(f)

    for index in enumerate(reader):
        print(index)
