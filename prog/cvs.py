import csv
import argparse

def sum_columns(csv_file, columns):
    sums = [0] * len(columns)  
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for i, col_index in enumerate(columns):
                try:
                    col_value = float(row[int(col_index)])
                    sums[i] += col_value
                except (ValueError, IndexError):
                    
                    pass
    
    return sums


def main():
    parser = argparse.ArgumentParser(prog="csv",
        description="Counts words, lines and characters of input files.")
    parser.add_argument("file", type=str, help="Takes file path to be processed")
    parser.add_argument("column", type=str, help="Takes file path to be processed")
    
    
    args = parser.parse_args()
    result = sum_columns(args.file, args.column)

    print("Sums of specified columns:", result[0])

if __name__ == "__main__":
    main()
