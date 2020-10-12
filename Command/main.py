from Command.CreateFile import CreateFile
from Command.ReadFile import ReadFile
from Command.RenameFile import RenameFile


# Zad 1
# Rozwiązanie w klasie CreateFile
# Zad 2
# Rozwiązanie w klasie RenameFile


def main():
    orig_name, new_name = 'file2', 'file3'
    commands = (CreateFile(orig_name),
                ReadFile(orig_name),
                RenameFile('falseName', new_name))
    [c.execute() for c in commands]
    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print("Error", str(e))


if __name__ == '__main__':
    main()
