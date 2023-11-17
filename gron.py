def format_json(data, path='json'):
    try:
        for key, value in data.items():
            print(f"{path}.{key} = {type(value)};")
            format_json(value, f"{path}.{key}")
    except AttributeError:
        try:
            for i, item in enumerate(data):
                print(f"{path}[{i}] = {type(item)};")
                format_json(item, f"{path}[{i}]")
        except TypeError:
            pass

# Your JSON data as a Python dictionary
input_json = {
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {"value": "New", "onclick": "CreateNewDoc()"},
                {"value": "Open", "onclick": "OpenDoc()"},
                {"value": "Close", "onclick": "CloseDoc()"}
            ]
        }
    }
}

format_json(input_json)
