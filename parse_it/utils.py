import os

def open_file_and_print(file):
    """
    Open a given file and print in terminal
    """
    with open(file, 'r') as outfile:
        print(outfile.read())

def open_given_file_and_append(line_to_write, file_to_write):
    """
    Function to append lines into provided file
    """
    with open(file_to_write, 'a+') as outfile:
        outfile.write(line_to_write)
        outfile.write('\n')