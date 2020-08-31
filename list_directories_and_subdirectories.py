# List all directories and subdirectories in a path
import os, argparse

# parser.add_argument(Variable_name, 
    # metavar=Name_of_the_parameter, 
    # type=Type_of_the_parameter, 
    # help=Help_string_displayed_with_-h)

parser = argparse.ArgumentParser(description="Write a list of all directories and subdirectories from the given path")
parser.add_argument("Path", metavar="path", type=str, help="the path to list")
parser.add_argument("Output_File", metavar="file_name", type=str, help="the name of the output file")

args = parser.parse_args()

output_file_name = args.Output_File
path = args.Path

output_file_name += ".txt"

a = open(output_file_name, "w")
for path, subdirs, files in os.walk(path):
    for filename in files:
        f = os.path.join(path, filename)
        a.write(str(f) + os.linesep)
