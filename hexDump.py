import binascii
import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()

currdir = os.getcwd()
tempdir = filedialog.askopenfile(
    parent=root, initialdir=currdir, title='Please select a File')


def splitAt(w, n):
    for i in range(0, len(w), n):
        yield w[i:i+n]


if __name__ == '__main__':
    if(tempdir):
        print("You chose {}".format(tempdir.name))
        print("File Dump: {}".format(tempdir.name))
        with open(tempdir.name, 'rb') as f:
            for chunk in iter(lambda: f.read(32), b''):
                x = binascii.hexlify(chunk)
                print(" ".join(splitAt(str(x.decode('utf-8')), 2)))
    else:
        print("No File Chosen")
