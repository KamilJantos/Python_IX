import os

verbose = True


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

### Dodanie sprawdzania, czy plik istnieje
    def execute(self):
        try:
            with open(self.src):
                rename(self.src, self.dest)
        except IOError:
            print('File does not exist')
            exit()

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


### utworzona dodatkowo funkcja
def rename(old_name, new_name):
    if verbose:
        print(f"[renaming '{old_name}' to '{new_name}']")
    os.rename(old_name, new_name)
