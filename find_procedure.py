import os

def print_result(dir_name, files):
    for file in files:
        print(os.path.join(dir_name, file))
    print('Всего: {}\n'.format(len(files)))

def search_string(path, files, string):
    find_files = []
    for file in files:
        with open(os.path.join(path, file), 'r') as f:
            if string in f.read():
                find_files.append(file)
    return find_files

def get_all_files(path):
    files = []
    for root, dirs, files_in_dir in os.walk(path):
        for filename in files_in_dir:
            if filename.endswith('.sql'):
                files.append(filename)
    return files

def main():
    dir_name = 'Migrations'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), dir_name)
    files = get_all_files(path)

    while True:
        string = input('Введите строку:')
        files = search_string(path, files, string)
        print_result(dir_name, files)

if __name__ == '__main__':
    main()