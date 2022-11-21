import pyAesCrypt
import os


def main():
    path_to_file = input('Enter the path to files: ')
    password = input('Enter the password for encrypt: ')
    walking_by_dirs(path_to_file, password)


def encryprion(file, password):
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + 'crp',
        password,
        buffer_size
    )
    print(f"Файл {str(os.path.splitext(file)[0])} зашифрован")

    os.remove(file)


def walking_by_dirs(path_to_file, password):
    for name in os.listdir(path_to_file):
        path = os.path.join(path_to_file, name)

        if os.path.isfile(path):
            try:
                encryprion(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(dir, password)


if __name__ == '__main__':
    main()
