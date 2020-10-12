import os

verbose = True


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        if does_exist(self.path):
            delete_file(self.path)


def delete_file(path):
    if verbose:
        print(f"deleting file {path}")
    os.remove(path)


### Funkcja does_exist
def does_exist(path):
    try:
        with open(path):
            return True
    except IOError:
        print('File does not exist')
        exit()
