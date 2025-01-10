import json

def write_file_override(path, *datas):
    with open(path, 'w') as f:
        for data in datas:
            f.write(data)

def write_file_append(path, *datas):
    with open(path, 'a') as f:
        for data in datas:
            f.write(data)

def write_file_as_json(path, *datas):
    with open(path, 'w') as f:
        for data in datas:
            json.dump(data, f)