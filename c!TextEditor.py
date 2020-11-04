import shutil

if __name__ == "__main__":
    original = r'C:\Users\PussyDestroyer\PycharmProjects\chezahernya\checker.py'

    with open("c!replace.txt") as file:
        array = [row.strip() for row in file]
        file.close()
    for n in range(1, 11, 1):
        target = 'C:/Users/PussyDestroyer/PycharmProjects/chezahernya/checker'
        name = 'checker'
        name += str(n)
        name += '.py'
        target += str(n)
        target += '.py'
        shutil.copyfile(original, target)
        data = "data = '"
        data += array[n-1]
        data += "'\n"
        with open(name, 'r') as f:
            get_all = f.readlines()
        with open(name, 'w') as f:
            for i, line in enumerate(get_all, 1):
                if i == 22:
                    f.writelines(data)
                else:
                    f.writelines(line)
