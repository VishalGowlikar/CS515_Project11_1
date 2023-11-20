import os
import subprocess

files_directory = "test"
files = os.listdir(files_directory)

def wc():
    global files_directory, files
    input_files = [file for file in files if file.endswith(".in") and "wc" in file]
    print(input_files)
    output_files = [file for file in files if file.endswith(".out") and "wc" in file]