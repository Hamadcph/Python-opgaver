import glob
import os


def getDirAndSub():
    a = open("output.txt", "w")
    for path, subdirs, files in os.walk(r'C:\\Users\\hamad\\OneDrive\\Dokumenter\\Datamatiker\\4.semester\\Python\\SemesterPlan\\Exercises\\OPGAVER\\uge2'):
        for filename in files:
            f = os.path.join(path, filename)
            a.write(str(f) + os.linesep)


getDirAndSub()


def read_first_line(file):

    with open(file, 'rt') as fd:
        first_line = fd.readline()
        print(first_line)
    return first_line
