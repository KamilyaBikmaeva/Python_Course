import pickle


def create_file():
    file_name = input('Enter filename: ')
    open(file_name, 'w').close()
    modify_file(file_name)


def modify_file(file_name=None):
    if file_name:
        with open(file_name, 'w') as file:
            lines_count = 0
            while True:
                inp = input(f'Enter something {lines_count + 1} : ')
                if inp == 'quit':
                    break
                file.write(inp+'\n')
                lines_count += 1
        save_metadata(lines_count, file_name)


def save_metadata(lines_entered, file_name=None):
    if file_name:
        with open(file_name + '_metadata.pkl', 'wb') as meta:
            pickle.dump((file_name, lines_entered), meta)


def load_metadata(file_name=None):
    if file_name:
        with open(file_name + '_metadata.pkl', 'rb') as meta:
            print(pickle.load(meta))


def open_file(file_name=None):
    if not file_name:
        file_name = input('Enter filename to open: ')
    with open(file_name + '_metadata.pkl', 'rb') as meta:
        print(pickle.load(meta))
    with open(file_name, 'r') as file:
        for line in file:
            print(line, end='')
