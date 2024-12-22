def Write(file, type):
    w=input()
    if type == 'write':
        f = open(file,'w')
        f.write(w)
        f.close()
    if type == 'dowrite':
        f = open(file,'a')
        f.write(w)
        f.close()
Write('example1.txt', 'dowrite')