import os


def scan(path):
    for name in os.listdir(path):
        full = os.path.join(path, name)

        print(full)

        if os.path.isdir(full):
            scan(full)


scan(".")