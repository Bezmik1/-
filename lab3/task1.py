def Screen(file, type):
    if type == 'line':
        f = open(file,'r')
        for line in f:
            print(line, end="")
            input()
    if type == 'all':
        f = open(file,'r')
        print(f.read())
Screen('example.txt', 'all')