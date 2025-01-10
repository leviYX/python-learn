import json

def readfile(path):
    try:
        with open(path) as file:
            content = file.read()
    except FileNotFoundError:
        print(f"the file {path} doesn't exist")
    else:
        print(content)

def readfile_and_print_line(path):
    try:
        with open(path) as file:
            for line in file:
                # # 每行的末尾都有一个看不见的换行符，而函数调用print() 也会加上一个换行符，因此每行末尾都有两个换行符：一个来自文件，另一个来自函数调用print() 。要消除这些多余的空白行，可在函数调用print() 中使用rstrip() ：
                print(line.rstrip())
    except FileNotFoundError:
        print(f"the file {path} doesn't exist")


def read_file_lines(path):
    try:
        with open(path) as file:
            lines = file.readline()
        for line in lines:
            print(line.rstrip())
    except FileNotFoundError:
        print(f"the file {path} doesn't exist")

def read_file_as_json(path):
    try:
        with open(path) as file:
            json_str = json.load(file)
    except FileNotFoundError:
        print(f"the file {path} doesn't exist")
    print(json_str)