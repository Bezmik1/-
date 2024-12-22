def Screen(file, type):
    if type == 'line':
        try:
            f = open(file,'r')
            for line in f:
                print(line, end="")
                input()
        except FileNotFoundError:
            print("не нашёл :(")
    if type == 'all':
        try:
            f = open(file,'r')
            print(f.read())
        except FileNotFoundError:
            print("не нашёл :(")
Screen('examphle.txt', 'all')