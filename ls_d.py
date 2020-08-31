# List all files in a path
import os
import argparse

# parser.add_argument(Variable_name, 
    # metavar=Name_of_the_parameter, 
    # type=Type_of_the_parameter, 
    # help=Help_string_displayed_with_-h)

parser = argparse.ArgumentParser(description="Write a list of all files in the given Path in the given output file")
parser.add_argument("Path", metavar="path", type=str, help="the path to list")
parser.add_argument("Output_File", metavar="file_name", type=str, help="the name of the output file")

args = parser.parse_args()

output_file_name = args.Output_File
path = args.Path

output_file_name += ".txt"

a = open(output_file_name, "w")
files = os.listdir(path)
for file in files:
    a.write(str(file) + '\n')

# List all directories and subdirectories in the path
# import os

