import json
import argparse
import sys

def print_json(json_obj, pre=''):
    if isinstance(json_obj, dict):
        if not pre:
            print("json = {};")
        for key, value in json_obj.items():
            if isinstance(value, dict):
                print(f"{pre}.{key} = {{}};")
                print_json(value, f"{pre}.{key}")
            elif isinstance(value, list):
                print(f"{pre}.{key} = [];")
                for i, item in enumerate(value):
                    print(f"{pre}.{key}[{i}] = {{}};")
                    print_json(item, f"{pre}.{key}[{i}]")
            else:
                print(f"{pre}.{key} = {json.dumps(value)};")
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            print(f"{pre}[{i}] = {{}};")
            print_json(item, f"{pre}[{i}]")

def main():
    parser = argparse.ArgumentParser(prog="gron",
        description="Counts words, lines and characters of input files.")
    parser.add_argument("file", type=str, help="Takes file path to be processed", default=str(sys.stdin))
    
    args = parser.parse_args()
    print(args)

    file_path = "eg.json"
    with open(args.file) as file:
        json_data = json.load(file)
        print_json(json_data)
    
if __name__ == "__main__":
    main()





