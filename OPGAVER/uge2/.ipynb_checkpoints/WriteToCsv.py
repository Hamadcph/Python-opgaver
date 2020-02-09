# def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
# rewrite the function so that it gets an arbitrary number of strings instead of a list
import csv
import platform

if platform.system() == 'Windows':
    newline = ''
else:
    newline = None


file_path = 'C:\\Users\\hamad\\OneDrive\\Dokumenter\\Datamatiker\\4.semester\\Python\\SemesterPlan\\Exercises\\OPGAVER\\uge2\\.ipynb_checkpoints\\test.csv'


with open(file_path, 'w', newline=newline) as output_file:
    output_writer = csv.writer(output_file)
    output_writer.writerow(['Hamad', 'Shah', 24])
    output_writer.writerow(['Jacob', 'Jabr', 23])
    output_writer.writerow(['Saz', 'Kazim', 22])
    output_writer.writerow(['Ali', 'Haider', 21])
