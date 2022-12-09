import os
def thumuc():
    x = input('nhap thu muc:')
    os.chdir(x)
    print('thu muc hien tai:',os.getcwd())
thumuc()